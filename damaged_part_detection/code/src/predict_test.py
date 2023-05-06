import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch

from Datasets import Datasets
from Models import Unet
from scipy import ndimage
from torch.utils.data import DataLoader

TEST_PATH = '../../data/custom/test'
SAVE_DIR = '../../data/result_log/predictions/'
WEIGHT_PATH = '../../data/weight/Unet_19.pt'
DATA_INFO = '../../data/datainfo/part_test.json'
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


def save_visual(origImage, origMask, predMask, img_ids):
    # initialize our figure
    figure, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 10))

    # plot the original image, its mask, and the predicted mask
    ax[0].imshow(origImage)
    ax[1].imshow(origImage,  cmap='gray')
    ax[1].imshow(origMask.permute(1, 2, 0), alpha=0.9)
    ax[2].imshow(origImage, cmap='gray')
    ax[2].imshow(predMask, alpha=0.9)

    # set the titles of the subplots
    ax[0].set_title("Image")
    ax[1].set_title("Original Mask")
    ax[2].set_title("Predicted Mask")

    # set the layout of the figure and display it
    figure.tight_layout()
    data = (predMask[:,:,0])
    plt.show()
    
    #figure.savefig(SAVE_DIR+str(img_ids))

def get_dataloader(dataset):
    eval_loader = DataLoader(
        dataset = dataset,
        shuffle = False, 
        num_workers = 0)
    
    return eval_loader


def make_predictions(model):

    parts = ["Front bumper","Rear bumper","Front fender(R)","Front fender(L)","Rear fender(R)","Trunk lid","Bonnet","Rear fender(L)","Rear door(R)","Head lights(R)","Head lights(L)","Front Wheel(R)","Front door(R)","Side mirror(R)"]
    model.eval()
    with torch.no_grad():
        
        test_datasets = Datasets(DATA_INFO, 'train', size = 256, label = None, one_channel = False, img_base_path = TEST_PATH)

        eval_data_loader = get_dataloader(test_datasets)
        
        for image, masks, img_ids in (eval_data_loader):
            print("IMAGE: " + img_ids[0])

            orig = image[0].permute(1, 2, 0).numpy().copy()
            image = image.clone().detach().float().to(DEVICE)

            predMask = model(image)
            predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
            predMask = np.transpose(predMask, (1,2,0))

            save_visual(orig, masks, predMask, img_ids[0])

            data_slices = ndimage.find_objects(predMask)
            
            try:
                if ((damage := data_slices[14]) != None):

                    y_start = damage[0].start
                    y_stop = damage[0].stop

                    x_start = damage[1].start
                    x_stop = damage[1].stop

                    cut = predMask[y_start:y_stop+1,x_start:x_stop+1,:]

                    (values,counts) = np.unique(cut,return_counts=True)
                    count_sort_ind = np.argsort(-counts)
                    for index in count_sort_ind:
                        if values[index] != 0 and values[index] != 15:
                            print("Damage detected at {}, area: {}%".format(parts[values[index]-1], round((counts[index] / cut.size) * 100, 1)))

                    # cv2.rectangle(orig, (int(x_start), int(y_start)), (int(x_stop), int(y_stop)), color=(0,0,255), thickness=3)
                    # cv2.imshow('resized', orig)

                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()

            except:
                print("Damage not detected")
            
            print("--------------------------------------------------------")

                


def load_model(weight_path):
    model = Unet(encoder="resnet34",pre_weight='imagenet',num_classes=16)
    model = model.to(DEVICE)
    try:
        model.model.load_state_dict(torch.load(weight_path, map_location=torch.device('cuda')))
        return model.model
    except:
        try:
            model.load_state_dict(torch.load(weight_path, map_location=torch.device('cpu')))
            return model
        except:
            model.load_state_dict(torch.load(weight_path, map_location=torch.device('cpu')), strict=False)
            return model


def main():
    print("[INFO] Visualizer for predicted images")
    print("[INFO] load up model...")
    model = load_model(weight_path=WEIGHT_PATH)
    make_predictions(model)
    print("[INFO] Completed")


if __name__ == '__main__':
    main()



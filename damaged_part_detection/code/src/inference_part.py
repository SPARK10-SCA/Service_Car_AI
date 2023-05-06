import cv2
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import torch
from Models import Unet
from scipy import ndimage

INPUT_PATH = '../../data/custom/test/0000686_sc-1024573.jpg'
WEIGHT_PATH = '../../data/weight/Unet_19.pt'

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


def part_save_visual(orig, predMask, damageROI):
    # initialize our figure
    figure, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))

    # plot the original image, and the predicted mask
    ax[0].imshow(orig)
    ax[1].imshow(orig,  cmap='gray')
    ax[1].imshow(predMask, alpha=0.9)

    if damageROI is not None:
        rect = patches.Rectangle((damageROI[0], damageROI[3]), damageROI[2]-damageROI[0], damageROI[1]-damageROI[3], linewidth=1, edgecolor='r', facecolor='none')
        ax[1].add_patch(rect)

    # set the titles of the subplots
    ax[0].set_title("Original")
    ax[1].set_title("Predicted Part")

    # set the layout of the figure and display it
    figure.tight_layout()
    
    plt.show()

def find_part(predMask):
    parts = ["Front bumper","Rear bumper","Front fender(R)","Front fender(L)","Rear fender(R)","Trunk lid","Bonnet","Rear fender(L)","Rear door(R)","Head lights(R)","Head lights(L)","Front Wheel(R)","Front door(R)","Side mirror(R)"]

    # Find and print car part objects
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

            # damage ROI
            return (x_start, y_start, x_stop, y_stop)

    except:
        print("Damage not detected")


def make_part_predictions(model):
    model.eval()
    with torch.no_grad():
        image = cv2.imread(INPUT_PATH)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (256,256))
        orig = image.copy()

        image = image.transpose([2,0,1]) 
        image = image/255.
        image = torch.tensor(image).float().to(DEVICE)

        predMask = model(image.unsqueeze(0))
        predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
        predMask = np.transpose(predMask, (1,2,0))

        damageROI = find_part(predMask)

        part_save_visual(orig, predMask, damageROI)


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
    print("[INFO] Inference for car part prediction")
    model = load_model(weight_path=WEIGHT_PATH)
    make_part_predictions(model)
    print("Completed!\n")

if __name__ == '__main__':
    main()
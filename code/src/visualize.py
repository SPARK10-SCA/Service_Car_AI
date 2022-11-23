import matplotlib.pyplot as plt
import numpy as np
import torch
import os
import glob

from Models import Unet
from Datasets import Datasets
from torch.utils.data import DataLoader

TEST_PATH = '../../data/custom/test/img'
SAVE_DIR = '../../data/result_log/predictions/break/'
WEIGHT_PATH = '../../data/weight/[DAMAGE][Breakage_3]Unet.pt'
DATA_INFO = '../../data/datainfo/damage_test.json'
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


def save_visual(origImage, origMask, predMask, img_ids):
    # initialize our figure
    figure, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 10))

    # plot the original image, its mask, and the predicted mask
    ax[0].imshow(origImage)
    ax[1].imshow(origMask.permute(1, 2, 0))
    ax[2].imshow(predMask)

    # set the titles of the subplots
    ax[0].set_title("Image")
    ax[1].set_title("Original Mask")
    ax[2].set_title("Predicted Mask")

    # set the layout of the figure and display it
    figure.tight_layout()
    
    #plt.show()
    
    figure.savefig(SAVE_DIR+str(img_ids))

def get_dataloader(dataset):
    eval_loader = DataLoader(
        dataset = dataset,
        shuffle = False, 
        num_workers = 0)
    
    return eval_loader


def make_predictions(model):
    model.eval()
    with torch.no_grad():
        
        test_datasets = Datasets(DATA_INFO, 'train', size = 256, label = None, one_channel = False, img_base_path = TEST_PATH)

        eval_data_loader = get_dataloader(test_datasets)
        
        for image, masks, img_ids in (eval_data_loader):

            orig = image[0].permute(1, 2, 0).numpy().copy()
            image = torch.tensor(image).float().to(DEVICE)

            predMask = model(image)
            predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
            predMask = np.transpose(predMask, (1,2,0))

            save_visual(orig, masks, predMask, img_ids[0])

def load_model(weight_path):
    model = Unet(encoder="resnet34",pre_weight='imagenet',num_classes=2)
    model = model.to(DEVICE)
    model.model.load_state_dict(torch.load(weight_path, map_location=torch.device('cuda')))
    return model.model



def main():
    print("[INFO] Visualizer for predicted images")
    print("[INFO] load up model...")
    model = load_model(weight_path=WEIGHT_PATH)
    make_predictions(model)
    print("[INFO] Completed")


if __name__ == '__main__':
    main()



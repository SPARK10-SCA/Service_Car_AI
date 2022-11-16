import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2
import os
import glob

from src.Models import Unet
from src.Datasets import Datasets
from torch.utils.data import DataLoader



TEST_PATH = 'data/custom/test'
WEIGHT_PATH = 'data/weight/Unet_part_start_2022-11-15_21_09_33_KST+0900_49_epoch_IoU_0.09.pt'
DEVICE = 'cpu'



def prepare_plot(origImage, origMask, predMask):
    # initialize our figure
    figure, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 10))
    # plot the original image, its mask, and the predicted mask
    ax[0].imshow(origImage)
    origMask = origMask.permute(1, 2, 0)
    ax[1].imshow(origMask)
    ax[2].imshow(predMask)
    # set the titles of the subplots
    ax[0].set_title("Image")
    ax[1].set_title("Original Mask")
    ax[2].set_title("Predicted Mask")
    # set the layout of the figure and display it
    figure.tight_layout()
    figure.show()

def get_dataloader(dataset):
    def collate_fn(batch):
        return tuple(zip(*batch))
    
    eval_loader = DataLoader(
        dataset = dataset,
        shuffle = False, 
        num_workers = 0)
        
    
    return eval_loader


def make_predictions(model, imagePath):
    # set model to evaluation mode
    model.eval()
    # turn off gradient tracking
    with torch.no_grad():
        # load the image from disk, swap its color channels, cast it
        # to float data type, and scale its pixel values    
        # 
            
        test_datasets = Datasets("data/datainfo/part_test.json", 'train', size = 256, label = None, one_channel = False, img_base_path = 'data/custom/img')

        eval_data_loader = get_dataloader(test_datasets)
        
        for step, (image, masks, _) in enumerate(eval_data_loader):

            #image = cv2.imread(imagePath)
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #image = image.astype("float32") / 255.0
            # resize the image and make a copy of it for visualization
            #image = cv2.resize(image, (128, 128))
            orig = image[0].permute(1, 2, 0).numpy().copy()


            # fig = plt.figure()
            # ax1 = fig.add_subplot(1,2,1)
            # ax1.imshow(images[0].permute(1, 2, 0).numpy())
            # ax1 = fig.add_subplot(1,2,2)
            # ax1.imshow(masks.permute(1, 2, 0))
            # fig.show()        
            #masks = cv2.resize(masks, (255,255))

            #image = np.transpose(image, (2,0,1))
            #image = np.expand_dims(image, 0)
            image = torch.tensor(image).float().to(DEVICE)

            predMask = model(image)
            predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
            #predMask = torch.argmax(predMask, dim=-1).detach().cpu()
            predMask = np.transpose(predMask, (1,2,0))
            



            # predMask = model(image).squeeze()
            # predMask = torch.argmax(predMask, dim=-1).detach().cpu().numpy()
            #predMask = (predMask > 0.1) * 255
            #predMask = predMask.astype(np.uint8)

            prepare_plot(orig, masks, predMask)

        # # find the filename and generate the path to ground truth
        # # mask
        # filename = imagePath.split(os.path.sep)[-1]
        # groundTruthPath = os.path.join(config.MASK_DATASET_PATH,
        # 	filename)
        # # load the ground-truth segmentation mask  in grayscale mode
        # # and resize it
        # gtMask = cv2.imread(groundTruthPath, 0)
        # gtMask = cv2.resize(gtMask, (config.INPUT_IMAGE_HEIGHT,
        # 	config.INPUT_IMAGE_HEIGHT))

        # # make the channel axis to be the leading one, add a batch
        # # dimension, create a PyTorch tensor, and flash it to the
        # # current device
        # image = np.transpose(image, (2, 0, 1))
        # image = np.expand_dims(image, 0)
        # image = torch.from_numpy(image).to(DEVICE)
        # # make the prediction, pass the results through the sigmoid
        # # function, and convert the result to a NumPy array
        # predMask = model(image).squeeze()
        # predMask = torch.sigmoid(predMask)
        # predMask = predMask.cpu().numpy()
        # # filter out the weak predictions and convert them to integers
        # predMask = (predMask > config.THRESHOLD) * 255
        # predMask = predMask.astype(np.uint8)
        # # prepare a plot for visualization
        # prepare_plot(orig, gtMask, predMask)

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


# load the image paths in our testing file and randomly select 10
# image paths
print("[INFO] loading up test image paths...")
imagePaths =  glob.glob(os.path.join(TEST_PATH, r"*.jpg"))

# load our model from disk and flash it to the current device
print("[INFO] load up model...")
model = load_model(weight_path=WEIGHT_PATH)

# iterate over the randomly selected test image paths
# for path in imagePaths:
    # make predictions and visualize the results
make_predictions(model, imagePaths)
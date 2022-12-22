from Model_UNET import Unet
from Model_VGG19 import IntelCnnModel
import torch
import numpy as np
import cv2
from PIL import Image
from torchvision.transforms import ToTensor

import os
import math 
import time
import matplotlib.pyplot as plt

INPUT_PATH = '../input/'
OUTPUT_PATH = '../output/'

PART_WEIGHT = '../weights/part/Part.pt'

BREAKAGE_WEIGHT = '../weights/damage/Breakage.pt'
CRUSHED_WEIGHT = '../weights/damage/Crushed.pt'
SCRATCHED_WEIGHT = '../weights/damage/Scratched.pt'
SEPARATED_WEIGHT = '../weights/damage/Separated.pt'

SEVERITY_WEIGHT = '../weights/severity/Severity.pth'

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def part_save_visual(orig, predMask):
    # initialize our figure
    figure, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))

    # plot the original image, its mask, and the predicted mask
    ax[0].imshow(orig)
    ax[1].imshow(predMask)

    # set the titles of the subplots
    ax[0].set_title("Original")
    ax[1].set_title("Part")

    # set the layout of the figure and display it
    figure.tight_layout()
    
    #plt.show()
    
    figure.savefig(OUTPUT_PATH+'part/part_api_output.jpg')

def damage_save_visual(orig, predMask1, predMask2, predMask3, predMask4):
    # initialize our figure
    figure, ax = plt.subplots(nrows=2, ncols=4, figsize=(10, 10))

    # plot the original image, its mask, and the predicted mask
    ax[0][0].imshow(orig)
    ax[0][1].axis('off')
    ax[0][2].axis('off')
    ax[0][3].axis('off')

    ax[1][0].imshow(predMask1)
    ax[1][1].imshow(predMask2)
    ax[1][2].imshow(predMask3)
    ax[1][3].imshow(predMask4)

    # set the titles of the subplots
    ax[0][0].set_title("Original")

    ax[1][0].set_title("Breakage")
    ax[1][1].set_title("Crushed")
    ax[1][2].set_title("Scratched")
    ax[1][3].set_title("Separated")

    # set the layout of the figure and display it
    figure.tight_layout()
    
    #plt.show()
    
    figure.savefig(OUTPUT_PATH+'damage/damage_api_output.jpg')

def make_part_predictions(model):
    model.eval()
    with torch.no_grad():
        #l = [file for file in os.listdir(INPUT_PATH) if file.endswith('.jpg')]
        image = Image.open(INPUT_PATH+'/'+'part_input.jpg')
        image = image.resize((256, 256))
        orig = image

        tf_toTensor = ToTensor()
        image = tf_toTensor(image).float().to(DEVICE)

        predMask = model(image.unsqueeze(0))
        predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
        predMask = np.transpose(predMask, (1,2,0))
        with open(OUTPUT_PATH+'part/predMask.txt', 'w') as outfile:
                for slice_2d in predMask:
                    np.savetxt(outfile, slice_2d)

        part_save_visual(orig, predMask)

def make_damage_predictions(model1, model2, model3, model4):
    model1.eval()
    model2.eval()
    model3.eval()
    model4.eval()
    with torch.no_grad():
        #l = [file for file in os.listdir(INPUT_PATH) if file.endswith('.jpg')]
        image = Image.open(INPUT_PATH+'/'+'damage_input.jpg')
        image = image.resize((256, 256))
        orig = image

        tf_toTensor = ToTensor()
        image = tf_toTensor(image).float().to(DEVICE) 
        
        image = torch.tensor(image).float().to(DEVICE)

        predMask1 = model1(image.unsqueeze(0))
        predMask1 = torch.argmax(predMask1, dim=1).detach().cpu().numpy()
        predMask1 = np.transpose(predMask1, (1,2,0))

        predMask2 = model2(image.unsqueeze(0))
        predMask2 = torch.argmax(predMask2, dim=1).detach().cpu().numpy()
        predMask2 = np.transpose(predMask2, (1,2,0))

        predMask3 = model3(image.unsqueeze(0))
        predMask3 = torch.argmax(predMask3, dim=1).detach().cpu().numpy()
        predMask3 = np.transpose(predMask3, (1,2,0))

        predMask4 = model4(image.unsqueeze(0))
        predMask4 = torch.argmax(predMask4, dim=1).detach().cpu().numpy()
        predMask4 = np.transpose(predMask4, (1,2,0))

        with open(OUTPUT_PATH+'damage/predMask1.txt', 'w') as outfile:
                for slice_2d in predMask1:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'damage/predMask2.txt', 'w') as outfile:
                for slice_2d in predMask2:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'damage/predMask3.txt', 'w') as outfile:
                for slice_2d in predMask3:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'damage/predMask4.txt', 'w') as outfile:
                for slice_2d in predMask4:
                    np.savetxt(outfile, slice_2d)

        damage_save_visual(orig, predMask1, predMask2, predMask3, predMask4)

def get_severity(model):
    l = [file for file in os.listdir(INPUT_PATH) if file.endswith('.jpg')]
    image = Image.open(INPUT_PATH+'/'+l[0])
    image = image.resize((256,256))

    tf_toTensor = ToTensor()
    image = tf_toTensor(image).float().to(DEVICE)
    
    predictions = model(image.unsqueeze(0))
    prediction = predictions[0].detach().cpu()
    severity = np.argmax(prediction)

    print(f"Car Damage Severity is Level {severity}\n")

def load_part_unet_model(weight_path):
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

def load_damage_unet_model(weight_path):
    model = Unet(encoder="resnet34",pre_weight='imagenet',num_classes=2)
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

'''def load_vgg_model():
    model = IntelCnnModel()
    model = model.to(DEVICE)
    return model.network;'''

def main():
    start = time.time()

    #part
    '''print("figuring out the damaged part...")
    model = load_part_unet_model(weight_path=PART_WEIGHT)
    make_part_predictions(model)
    print("Completed!\n")'''
    
    #damage
    print("figuring out the type of damage...")
    model1 = load_damage_unet_model(weight_path=BREAKAGE_WEIGHT)
    model2 = load_damage_unet_model(weight_path=CRUSHED_WEIGHT)
    model3 = load_damage_unet_model(weight_path=SCRATCHED_WEIGHT)
    model4 = load_damage_unet_model(weight_path=SEPARATED_WEIGHT)
    make_damage_predictions(model1, model2, model3, model4)
    print("Completed!\n")

    #severity
    '''print("figuring out the severity of damage...")
    model = torch.load("../weights/severity/Severity.pth")
    get_severity(model)'''

    end = time.time()
    print(f"{end - start:.5f} sec")

if __name__ == '__main__':
    main()
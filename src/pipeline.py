from Model_UNET import Unet
from Model_VGG19 import IntelCnnModel
import torch
import numpy as np
import cv2
from torch.utils.data import DataLoader
from pycocotools.coco import COCO
from torchvision.transforms import ToTensor
import albumentations as A
import torch.nn.functional as F

import os
import sys
from PIL import Image
from skimage import color
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.patches as patches

INPUT_PATH = '../input/'
OUTPUT_PATH = '../output/'

PART_WEIGHT = '../weights/part/Part.pt'

BREAKAGE_WEIGHT = '../weights/damage/Breakage.pt'
CRUSHED_WEIGHT = '../weights/damage/Crushed.pt'
SCRATCHED_WEIGHT = '../weights/damage/Scratched.pt'
SEPARATED_WEIGHT = '../weights/damage/Separated.pt'

SEVERITY_WEIGHT = '../weights/severity/Severity.pth'

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

def find_part(predMask):
    parts = ["Front bumper","Rear bumper","Front fender(R)","Front fender(L)","Rear fender(R)","Trunk lid","Bonnet","Rear fender(L)","Rear door(R)","Head lights(R)","Head lights(L)","Front Wheel(R)","Front door(R)","Side mirror(R)", "Damage"]

    # Find and print car part objects
    data_slices = ndimage.find_objects(predMask)
    coor = {}
    try:
        if ((damage := data_slices[14]) != None):

            y_start = damage[0].start
            y_stop = damage[0].stop

            x_start = damage[1].start
            x_stop = damage[1].stop

            coor[parts[14]] = (x_start, y_start, x_stop, y_stop)
           #coor.extend((x_start, y_start, x_stop, y_stop))

            cut = predMask[y_start:y_stop+1,x_start:x_stop+1,:]

            (values,counts) = np.unique(cut,return_counts=True)
            count_sort_ind = np.argsort(-counts)
            for index in count_sort_ind:
                if values[index] != 0 and values[index] != 15:
                    coor[parts[values[index]-1]] = (data_slices[values[index]-1][1].start, data_slices[values[index]-1][0].start, data_slices[values[index]-1][1].stop, data_slices[values[index]-1][0].stop)
                    #print("Part: {}, area: {}%".format(parts[values[index]-1], round((counts[index] / cut.size) * 100, 1)))

            return coor

    except:
        return None


def find_damage(predMask):
    # Find and print car part objects
    data_slices = ndimage.find_objects(predMask)
    try:
        if ((damage := data_slices[0]) != None):

            y_start = damage[0].start
            y_stop = damage[0].stop

            x_start = damage[1].start
            x_stop = damage[1].stop

            cut = predMask[y_start:y_stop+1,x_start:x_stop+1,:]

            val = round(cut.size/(256*256) * 100, 1)
            if val < 0.1: 
                return None
            else:
                return val 

    except:
        return None

def make_part_predictions(model, origImage):
    model.eval()
    with torch.no_grad():
    
        tf_toTensor = ToTensor()
        image = tf_toTensor(origImage).float().to(DEVICE)

        predMask = model(image.unsqueeze(0))
        predMask = torch.argmax(predMask, dim=1).detach().cpu().numpy()
        predMask = np.transpose(predMask, (1,2,0))
        
        '''with open(OUTPUT_PATH+'part/predMask.txt', 'w') as outfile:
                for slice_2d in predMask:
                    np.savetxt(outfile, slice_2d)'''

        coor = find_part(predMask)

        return (predMask, coor)

def make_damage_predictions(model1, model2, model3, model4, part_img):
    model1.eval()
    model2.eval()
    model3.eval()
    model4.eval()
    with torch.no_grad():
    
        tf_toTensor = ToTensor()
        image = tf_toTensor(part_img).float().to(DEVICE)

        predMask=[0,0,0,0]

        predMask[0] = model1(image.unsqueeze(0))
        predProb1 = F.softmax(predMask[0], dim = 1).detach().cpu().numpy()
        predMask[0] = torch.argmax(predMask[0], dim=1).detach().cpu().numpy()

        predMask[1] = model2(image.unsqueeze(0))
        predProb2 = F.softmax(predMask[1], dim = 1).detach().cpu().numpy()
        predMask[1] = torch.argmax(predMask[1], dim=1).detach().cpu().numpy()

        predMask[2] = model3(image.unsqueeze(0))
        predProb3 = F.softmax(predMask[2], dim = 1).detach().cpu().numpy()
        predMask[2] = torch.argmax(predMask[2], dim=1).detach().cpu().numpy()

        predMask[3] = model4(image.unsqueeze(0))
        predProb4 = F.softmax(predMask[3], dim = 1).detach().cpu().numpy()
        predMask[3] = torch.argmax(predMask[3], dim=1).detach().cpu().numpy()

        sum = [0,0,0,0]
        count = [0,0,0,0]
        for x in range(predMask[0].shape[1]):
            for y in range(predMask[0].shape[2]):
                if (predMask[0][0,x,y]):
                    count[0] += 1
                    sum[0] += predProb1[0,1,x,y]
                if (predMask[1][0,x,y]):
                    count[1] += 1
                    sum[1] += predProb2[0,1,x,y]
                if (predMask[2][0,x,y]):
                    count[2] += 1
                    sum[2] += predProb3[0,1,x,y]
                if (predMask[3][0,x,y]):
                    count[3] += 1
                    sum[3] += predProb4[0,1,x,y]

        val=[0,0,0,0]

        predMask[0] = np.transpose(predMask[0], (1,2,0))
        val[0] = find_damage(predMask[0])

        predMask[1] = np.transpose(predMask[1], (1,2,0))
        val[1] = find_damage(predMask[1])

        predMask[2] = np.transpose(predMask[2], (1,2,0))
        val[2] = find_damage(predMask[2])

        predMask[3] = np.transpose(predMask[3], (1,2,0))
        val[3] = find_damage(predMask[3])


        '''with open(OUTPUT_PATH+'breakage_predMask.txt', 'w') as outfile:
                for slice_2d in predMask1:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'crushed_predMask.txt', 'w') as outfile:
                for slice_2d in predMask2:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'scratched_predMask3.txt', 'w') as outfile:
                for slice_2d in predMask3:
                    np.savetxt(outfile, slice_2d)

        with open(OUTPUT_PATH+'separated_predMask4.txt', 'w') as outfile:
                for slice_2d in predMask4:
                    np.savetxt(outfile, slice_2d)'''

    return (predMask, val, sum, count)

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

def get_severity(model, origImage):
    tf_toTensor = ToTensor()
    image = tf_toTensor(origImage).float().to(DEVICE)
    
    predictions = model(image.unsqueeze(0))
    prediction = predictions[0].detach().cpu()
    severity = np.argmax(prediction)

    return severity

def main():
    #load part model
    model = load_part_unet_model(weight_path=PART_WEIGHT)

    #load damage model
    model1 = load_damage_unet_model(weight_path=BREAKAGE_WEIGHT)
    model2 = load_damage_unet_model(weight_path=CRUSHED_WEIGHT)
    model3 = load_damage_unet_model(weight_path=SCRATCHED_WEIGHT)
    model4 = load_damage_unet_model(weight_path=SEPARATED_WEIGHT)

    #load severity model
    severity_model = torch.load(SEVERITY_WEIGHT)

    #load original image
    origImage = Image.open('../input/input.jpg')
    origImage = origImage.resize((256, 256))
    origImage.save("../input/input.png")

    #part_prediction
    part_mask, coor = make_part_predictions(model, origImage)
    parts = list(coor.keys())[1:]
    part_coor = []
    for part in parts:
        part_coor.append(coor[part])
    print("Damaged Parts: "+', '.join(parts))
    
    for i in range(len(parts)):
        print("\nDetecting damage in "+parts[i]+"...\n")
        crop = origImage.crop(part_coor[i])
        width, height = crop.size
        part_img = Image.new(crop.mode, (256,256), (255, 255, 255))
        part_img.paste(crop, (int((256-width)/2), int((256-height)/2)))
        
        figure, ax = plt.subplots(nrows=3, ncols=4, figsize=(15, 15))

        #original
        ax[0][0].imshow(origImage)
        ax[0][0].set_title("Original")

        ax[0][1].axis('off')
        ax[0][2].axis('off')
        ax[0][3].axis('off')

        #part 
        ax[1][0].imshow(origImage, cmap='gray')
        ax[1][0].imshow(color.label2rgb(part_mask[:,:,0]), alpha=0.4)
        ax[1][0].set_title("Damaged part")
        ax[1][1].axis('off')
        ax[1][2].axis('off')
        ax[1][3].axis('off')

        damage_mask, val, sum, count = make_damage_predictions(model1, model2, model3, model4, origImage)

        #damage
        ax[2][0].imshow(origImage, cmap='gray')
        ax[2][0].imshow(color.label2rgb(damage_mask[0][:,:,0]), alpha=1.0)
        ax[2][0].set_title("Breakage")

        ax[2][1].imshow(origImage, cmap='gray')
        ax[2][1].imshow(color.label2rgb(damage_mask[1][:,:,0]), alpha=1.0)
        ax[2][1].set_title("Crushed")

        ax[2][2].imshow(origImage, cmap='gray')
        ax[2][2].imshow(color.label2rgb(damage_mask[2][:,:,0]), alpha=1.0)
        ax[2][2].set_title("Scratched")

        ax[2][3].imshow(origImage, cmap='gray')
        ax[2][3].imshow(color.label2rgb(damage_mask[3][:,:,0]), alpha=1.0)
        ax[2][3].set_title("Separated")

        labels = ['Breakage', 'Crushed', 'Scratched', 'Separated']

        for j in range(4):
            if val[j] is None: 
                print(labels[j]+": Damage is not detected")
            else: 
                print(labels[j]+": "+str(val[i])+"% area")
                print(labels[j] + " confidence score: "+ str(round((sum[j]/count[j]) * 100, 1)) + "%")

            print("")
        
        severity = get_severity(severity_model, part_img)
        print(parts[i]+" damage severity is level "+str(int(severity)))

        #figure.tight_layout()
        figure.savefig('../output/'+parts[i]+'_api.jpg')
        print("\n"+"-"*40)


def test():
    #load part model
    model = load_part_unet_model(weight_path=PART_WEIGHT)

    #load damage model
    model1 = load_damage_unet_model(weight_path=BREAKAGE_WEIGHT)
    model2 = load_damage_unet_model(weight_path=CRUSHED_WEIGHT)
    model3 = load_damage_unet_model(weight_path=SCRATCHED_WEIGHT)
    model4 = load_damage_unet_model(weight_path=SEPARATED_WEIGHT)

    #load severity model
    severity_model = torch.load(SEVERITY_WEIGHT)

    #enter index
    print("Enter the index (1-1000): ", end="")
    idx = int(input())
    l = [file for file in os.listdir("../testset/img/")]

    #load original mask
    coco = COCO('../testset/datainfo/testset_info.json')
    img_ids = coco.getImgIds()
    image_id = int(img_ids[idx])
    image_infos = coco.loadImgs(image_id)[0]
    images = cv2.imread(os.path.join('../testset/img/', image_infos['file_name']))
    images = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    ann_ids = coco.getAnnIds(imgIds=image_infos['id'])
    anns = coco.loadAnns(ann_ids)
    masks = np.zeros((image_infos["height"], image_infos["width"]))
    for ann in anns:
        pixel_value = ann['category_id'] + 1
        masks = np.maximum(coco.annToMask(ann) * pixel_value, masks)
    resize = A.Compose([A.Resize(width=256, height=256)])
    transformed = resize(image = images, mask=masks)
    origMask = transformed["mask"]

    #load original image
    origImage = Image.open(os.path.join('../testset/img/', image_infos['file_name']))
    origImage = origImage.resize((256, 256))
    origImage.save("../input/test_input.jpg")

    #part_prediction
    part_mask, coor = make_part_predictions(model, origImage)
    parts = list(coor.keys())[1:]
    part_coor = []
    for part in parts:
        part_coor.append(coor[part])
    print("Damaged Parts: "+', '.join(parts))

    for i in range(len(parts)):
        print("\nDetecting damage in "+parts[i]+"...\n")
        crop = origImage.crop(part_coor[i])
        width, height = crop.size
        part_img = Image.new(crop.mode, (256,256), (255, 255, 255))
        part_img.paste(crop, (int((256-width)/2), int((256-height)/2)))
        
        figure, ax = plt.subplots(nrows=3, ncols=4, figsize=(15, 15))

        #original
        ax[0][0].imshow(origImage)
        ax[0][0].set_title("Original")

        ax[0][1].imshow(origImage, cmap='gray')
        ax[0][1].imshow(origMask, alpha=0.4)
        ax[0][1].set_title("Answer Mask")

        ax[0][2].axis('off')
        ax[0][3].axis('off')

        #part 
        ax[1][0].imshow(origImage, cmap='gray')
        ax[1][0].imshow(color.label2rgb(part_mask[:,:,0]), alpha=0.4)
        ax[1][0].set_title("Damaged part")
        ax[1][1].axis('off')
        ax[1][2].axis('off')
        ax[1][3].axis('off')

        damage_mask, val, sum, count = make_damage_predictions(model1, model2, model3, model4, origImage)

        #damage
        #ax[2][0].imshow(part_img, cmap='gray')
        ax[2][0].imshow(color.label2rgb(damage_mask[0][:,:,0]))
        ax[2][0].set_title("Breakage")

        #ax[2][1].imshow(part_img, cmap='gray')
        ax[2][1].imshow(color.label2rgb(damage_mask[1][:,:,0]))
        ax[2][1].set_title("Crushed")

        #ax[2][2].imshow(part_img, cmap='gray')
        ax[2][2].imshow(color.label2rgb(damage_mask[2][:,:,0]))
        ax[2][2].set_title("Scratched")

        #ax[2][3].imshow(part_img, cmap='gray')
        ax[2][3].imshow(color.label2rgb(damage_mask[3][:,:,0]))
        ax[2][3].set_title("Separated")

        labels = ['Breakage', 'Crushed', 'Scratched', 'Separated']

        for j in range(4):
            if val[j] is None: 
                print(labels[j]+": Damage is not detected")
            else: 
                print(labels[j]+": "+str(val[i])+"% area")
                print(labels[j] + " confidence score: "+ str(round((sum[j]/count[j]) * 100, 1)) + "%")
            
            print("")
        
        severity = get_severity(severity_model, part_img)
        print(parts[i]+" damage severity is level "+str(int(severity)))

        #figure.tight_layout()
        figure.savefig('../output/'+parts[i]+'_test.jpg')
        print("\n"+"-"*40)  

if __name__ == '__main__':
    if len(sys.argv) == 1: main()
    elif sys.argv[1]=="test": test()

    
"""
    cropBBox - Python code to crop and save the bounding box annotations for images
    Saves the cropped images in given destination dir
    
    Modify - path, images_path, dst_dir for custom images 
    OUTPUT - cropped images in dst_dir/1,2,3,4 according to levels
"""

import json
from pycocotools.coco import COCO
import cv2
import os

# path: images' json files in coco format
# images_path: image directory path

path = "../../data/datainfo/part_test.json"
images_path = "../../data/custom/test/"
dst_dir = "../../data/severity/"


# Store img file names
img_names = []
f = open(path)
data = json.load(f)
for i in data['images']:
    img_names.append(i['file_name'])  

# Load coco format annotations
coco=COCO(path)
image_ids = coco.getImgIds()
annotation_ids = coco.getAnnIds()
anns = coco.loadAnns(annotation_ids)


# Draw boxes and add label to each box
for ann in anns:

    # create destination directories 
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if not os.path.exists(dst_dir + '/1'):
        os.makedirs(dst_dir + '/1')
    if not os.path.exists(dst_dir + '/2'):
        os.makedirs(dst_dir + '/2')
    if not os.path.exists(dst_dir + '/3'):
        os.makedirs(dst_dir + '/3')
    if not os.path.exists(dst_dir + '/4'):
        os.makedirs(dst_dir + '/4')

    if ann['level'] != None:
        image = cv2.imread(images_path + img_names[ann['image_id']-1])
        #print("Dest: " + dst_dir+str(ann['level']) + '/'+ img_names[ann['image_id']-1].replace(".jpg", "")+'_'+ann['part'].replace(' ','')+'.jpg')

        try: # for invalid bounding boxes
            [x,y,w,h] = ann['bbox']
            cropped_image = image[y:y+h,x:x+w]
            
            resized_image = cv2.resize(cropped_image, (244, 244)) 
            cv2.imwrite(dst_dir+str(ann['level']) + '/'+ img_names[ann['image_id']-1].replace(".jpg", "")+'_'+ann['part'].replace(' ','')+'.jpg', resized_image)
        except:
            pass


print("Cropped Done")
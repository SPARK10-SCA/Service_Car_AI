"""
    visualizeBBox - Python code to visualize the bounding box annotations for images
    Displays images with rectangles indicating bounding boxes
    
    Modify - path, images_path for custom images 
    OUTPUT - cv2 images
"""

import json
from pycocotools.coco import COCO
import cv2

# path: images' json files in coco format
# images_path: image directory path

path = "../../data/datainfo/part_test.json"
images_path = "../../data/custom/test/"

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
    if ann['level'] != None: # draw bounding box for those with levels. remove for all bounding boxes
        image = cv2.imread(images_path + img_names[ann['image_id']-1])
        [x,y,w,h] = ann['bbox']
        
        cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), color=(0,0,255), thickness=3)
        cv2.imshow('resized', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


import json
from pycocotools.coco import COCO


path = "data/datainfo/part_test.json"

coco=COCO(path)
image_ids = coco.getImgIds()
#print(image_ids)
annotation_ids = coco.getAnnIds(imgIds=1)
anns = coco.loadAnns(annotation_ids)

for ann in anns:
    print(ann['bbox'])

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
 
image_id = 196610
 
images_path = "data/custom/test/0000686_sc-1024573.jpg"
image = Image.open(images_path)
 
fig, ax = plt.subplots()
 
# Draw boxes and add label to each box
for ann in anns:
    box = ann['bbox']
    bb = patches.Rectangle((box[0],box[1]), box[2],box[3], linewidth=2, edgecolor="blue", facecolor="none")
    ax.add_patch(bb)
 
ax.imshow(image)
plt.show()
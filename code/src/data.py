from pycocotools.coco import COCO
import cv2
import skimage.io as io
import matplotlib.pyplot as plt
import json

f = open('data/datainfo/part_train.json')
ann = json.load(f)
count = 0
cat_arr = [0] * 15
for a in ann['annotations']:
    cat_arr[a['category_id']] += 1

l_sch = ["Front bumper","Rear bumper","Front fender(R)","Front fender(L)","Rear fender(R)","Trunk lid","Bonnet","Rear fender(L)","Rear door(R)","Head lights(R)","Head lights(L)","Front Wheel(R)","Front door(R)","Side mirror(R)", "etc"]


plt.bar(l_sch, cat_arr)

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()


print(cat_arr)
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
import pandas as pd
import openpyxl

ann_path = "./data/datainfo/severity_all.json"
images_path = "/home/work/AIHUB/1.Training/1.원천데이터/damage_part/"
file_path = "/home/work/AIHUB/1.Training/1.원천데이터/TS_99.붙임_견적서/"
dst_dir = "./data/img/"

def padding(img, set_size):

    try:
        h,w,c = img.shape
    except:
        print('파일을 확인후 다시 시작하세요.')
        raise

    if h < w:
        new_width = set_size
        new_height = int(new_width * (h/w))
    else:
        new_height = set_size
        new_width = int(new_height * (w/h))

    if max(h, w) < set_size:
        img = cv2.resize(img, (new_width, new_height), cv2.INTER_CUBIC)
    else:
        img = cv2.resize(img, (new_width, new_height), cv2.INTER_AREA)

 
    try:
        h,w,c = img.shape
    except:
        print('파일을 확인후 다시 시작하세요.')
        raise

    delta_w = set_size - w
    delta_h = set_size - h
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    return new_img

def classification(ann):
    level = '/'
    img_id = img_names[ann['image_id']-1].replace(".jpg", "")
    part = ann['part'].replace(' ','')

    # Store xls file
    xls_path = file_path + img_id.split("_")[1] + '.xls'
    xls = pd.read_excel(xls_path, usecols=[2, 4], skiprows=range(0, 22))

    if xls.empty:
        return False
    
    xls.columns = ['part', 'level']
    # Translate part name and match
    if part == 'Frontbumper':
        _xls = xls[xls['part'].str.contains('프런트범퍼|프런트 범퍼|앞범퍼|후론트 범퍼|후론트범퍼')]
    elif part == 'Rearbumper':
        _xls = xls[xls['part'].str.contains('리어범퍼|리어 범퍼|뒤범퍼')]
    elif part == 'Frontfender(R)':
        _xls = xls[xls['part'].str.contains('프런트펜더(우)|프런트휀다(우)|앞펜더(우)|앞휀다(우)|앞휀더(우)|후론트휀다(우)|후론트 휀다(우)')]
    elif part == 'Frontfender(L)':
        _xls = xls[xls['part'].str.contains('프런트펜더(좌)|프런트 펜더(좌)|프런트휀다(좌)|앞펜더(좌)|앞휀다(좌)|앞휀더(좌)|후론트휀다(좌)|후론트 휀다(좌)')]
    elif part == 'Rearfender(R)':
        _xls = xls[xls['part'].str.contains('리어펜더(우)|리어휀다(우)|리어 휀다(우)|뒤펜더(우)|뒤휀다(우)|뒤휀더(우)')]
    elif part == 'Trunklid':
        _xls = xls[xls['part'].str.contains('트렁크')]
    elif part == 'Bonnet':
        _xls = xls[xls['part'].str.contains('본넷|본네트')]
    elif part == 'Rearfender(L)':
        _xls = xls[xls['part'].str.contains('리어펜더(좌)|리어휀다(좌)|리어 휀다(좌)|뒤펜더(좌)|뒤휀다(좌)|뒤휀더(좌)')]
    elif part == 'Reardoor(R)':
        _xls = xls[xls['part'].str.contains('리어도어|도어(뒤')]
    elif part == 'Headlights(R)':
        _xls = xls[xls['part'].str.contains('헤드라이트(우)|헤드램프(우)')]
    elif part == 'Headlights(L)':
        _xls = xls[xls['part'].str.contains('헤드라이트(좌)|헤드램프(좌)')]
    elif part == 'FrontWheel(R)':
        _xls = xls[xls['part'].str.contains('휠')]
    elif part == 'Frontdoor(R)':
        _xls = xls[xls['part'].str.contains('프런트도어|도어(앞|후론트 도어')]
    elif part == 'Sidemirror(R)':
        _xls = xls[xls['part'].str.contains('사이드미러')]
    else: # part is not exist in categories
        return False
    
    # level classfication
    if _xls.empty: # is not exist in 견적서
        return False
    else:
        if _xls['level'][0] == '교환':
            level = 'high/'
        elif _xls['level'][0] == '수리' or _xls['level'][0] == '판금' or _xls['level'][0] == '오버홀':
            level = 'medium/'
        elif _xls['level'][0] == '도장' or _xls['level'][0] == '탈착' or _xls['level'][0] == '1/2OH':
            level = 'low/'
    
    if level=='/':
        return False

    return dst_dir + level + img_id +'_'+ part +'.jpg'


# Store img file names
img_names = []
f = open(ann_path)
data = json.load(f)
for i in data['images']:
    img_names.append(i['file_name'])

# Load coco format annotations
coco=COCO(ann_path)
image_ids = coco.getImgIds()
annotation_ids = coco.getAnnIds()
anns = coco.loadAnns(annotation_ids)

# create destination directories 
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

if not os.path.exists(dst_dir+'high'):
    os.makedirs(dst_dir+'high')

if not os.path.exists(dst_dir+'medium'):
    os.makedirs(dst_dir+'medium')

if not os.path.exists(dst_dir+'low'):
    os.makedirs(dst_dir+'low')

# Draw boxes and add label to each box
for ann in anns:
    
    image = cv2.imread(images_path + img_names[ann['image_id']-1])
    #print("Dest: " + dst_dir+ img_names[ann['image_id']-1].replace(".jpg", "")+'_'+ann['part'].replace(' ','')+'.jpg')

    try: # for invalid bounding boxes
        [x,y,w,h] = ann['bbox']
        cropped_image = image[y:y+h,x:x+w]
        padding_image = padding(cropped_image, 244)
        if ann['part'] != None:
            dst = classification(ann)
            if dst == False:
                pass
            else:
                cv2.imwrite(dst, padding_image)
    except:
        pass


print("Done")
import os
import shutil
import json

dir_file = r'./data/custom/train/'
dir_breakage = dir_file+'Breakage/'
dir_crushed = dir_file+'Crushed/'
dir_scratched = dir_file+'Scratched/'
dir_separated = dir_file+'Separated/'


form = r'.json'
l = [file for file in os.listdir(dir_file) if file.endswith(form)]

cnt=0

for item in l:
    cnt_break=0
    cnt_crush=0
    cnt_scratch=0
    cnt_separate=0
    with open(dir_file+item) as f:
        obj = json.load(f)
        len_ann = len(obj['annotations'])
        for i in range(len_ann):
            if obj['annotations'][i]['damage']=='Breakage' and cnt_break==0:
                shutil.copyfile(dir_file+item, dir_breakage+item)
                jpg = item.replace('.json', '.jpg')
                shutil.copyfile(dir_file+jpg, dir_breakage+jpg)
                cnt_break+=1
            elif obj['annotations'][i]['damage']=='Crushed' and cnt_crush==0:
                shutil.copyfile(dir_file+item, dir_crushed+item)
                jpg = item.replace('.json', '.jpg')
                shutil.copyfile(dir_file+jpg, dir_crushed+jpg)
                cnt_crush+=1
            elif obj['annotations'][i]['damage']=='Scratched' and cnt_scratch==0:
                shutil.copyfile(dir_file+item, dir_scratched+item)
                jpg = item.replace('.json', '.jpg')
                shutil.copyfile(dir_file+jpg, dir_scratched+jpg)
                cnt_scratch+=1
            elif obj['annotations'][i]['damage']=='Separated' and cnt_separate==0:
                shutil.copyfile(dir_file+item, dir_separated+item)
                jpg = item.replace('.json', '.jpg')
                shutil.copyfile(dir_file+jpg, dir_separated+jpg)
                cnt_separate+=1
        cnt+=1

print(cnt, 'files classify completed')
                

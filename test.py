import os

dir = r'./data/custom/train'
form1 = r'.json'
form2 = r'.jpg'

l1 = [file for file in os.listdir(dir) if file.endswith(form1)]
l2 = [file for file in os.listdir(dir) if file.endswith(form2)]

l = []

for item in l1:
    item = item.replace('.json','.jpg')
    if item not in l2: 
        item = item.replace('.jpg', '.json')
        l.append(item)
        os.remove(dir+'/'+item)
        
print(len(l))

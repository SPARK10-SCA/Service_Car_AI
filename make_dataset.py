import os
import shutil
import random

data_dir = './data/img/'
train_dir = './data/train/'
valid_dir = './data/val/'
test_dir = './data/test/'

def reset_dir():
    if os.path.exists(train_dir+'high/'):
        shutil.rmtree(train_dir+'high')
        shutil.rmtree(train_dir+'medium')
        shutil.rmtree(train_dir+'low')

    if os.path.exists(valid_dir+'high/'):
        shutil.rmtree(valid_dir+'high')
        shutil.rmtree(valid_dir+'medium')
        shutil.rmtree(valid_dir+'low')

    if os.path.exists(test_dir+'high/'):
        shutil.rmtree(test_dir+'high')
        shutil.rmtree(test_dir+'medium')
        shutil.rmtree(test_dir+'low')

def copy_to_train():
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(train_dir+'high/'):
        os.makedirs(train_dir+'high/')
    if not os.path.exists(train_dir+'medium/'):
        os.makedirs(train_dir+'medium/')
    if not os.path.exists(train_dir+'low/'):
        os.makedirs(train_dir+'low/')

    high = [file for file in os.listdir(data_dir+'high/') if file.endswith('.jpg')]
    for file in high:
        shutil.copy(data_dir+'high/'+file, train_dir+'high/'+file)
    medium = [file for file in os.listdir(data_dir+'medium/') if file.endswith('.jpg')]
    for file in medium:
        shutil.copy(data_dir+'medium/'+file, train_dir+'medium/'+file)
    low = [file for file in os.listdir(data_dir+'low/') if file.endswith('.jpg')]
    for file in low:
        shutil.copy(data_dir+'low/'+file, train_dir+'low/'+file)
    
    print("Done copy_to_train")

def confirm_train():
    hdict={}
    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    for file in high:
        part = file.split('_')[2]
        way = file.split('_')[3]
        if part in hdict: hdict[part]+=1
        else: hdict[part]=1
        if way in hdict: hdict[way]+=1
        else: hdict[way]=1
    mdict={}
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    for file in medium:
        part = file.split('_')[2]
        way = file.split('_')[3]
        if part in mdict: mdict[part]+=1
        else: mdict[part]=1
        if way in mdict: mdict[way]+=1
        else: mdict[way]=1
    ldict={}
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    for file in low:
        part = file.split('_')[2]
        way = file.split('_')[3]
        if part in ldict: ldict[part]+=1
        else: ldict[part]=1
        if way in ldict: ldict[way]+=1
        else: ldict[way]=1
    
    print(hdict)
    print(mdict)
    print(ldict)
    print("Done confirm_train")

def remove_random():
    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    cnt=len(high)
    while cnt>7600:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'high/'+high[rand]) 
            high.pop(rand)
            cnt-=1
        except:
            pass
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    cnt=len(medium)
    while cnt>7600:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'medium/'+medium[rand])
            medium.pop(rand)
            cnt-=1
        except:
            pass       
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    cnt=len(low)
    while cnt>7600:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'low/'+low[rand])
            low.pop(rand)
            cnt-=1
        except:
            pass
       
    print("Done remove_random")

def remove_custom():
    high1 = [file for file in os.listdir(train_dir+'high/') if 'Frontbumper' in file]
    high2 = [file for file in os.listdir(train_dir+'high/') if 'Rearbumper' in file]
    cnt=len(high1)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'high/'+high1[rand]) 
            high1.pop(rand)
            cnt-=1
        except:
            pass
    cnt=len(high2)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'high/'+high2[rand]) 
            high2.pop(rand)
            cnt-=1
        except:
            pass
    medium1 = [file for file in os.listdir(train_dir+'medium/') if 'Frontbumper' in file]
    medium2 = [file for file in os.listdir(train_dir+'medium/') if 'Rearbumper' in file]
    cnt=len(medium1)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'medium/'+medium1[rand])
            medium1.pop(rand)
            cnt-=1
        except:
            pass    
    cnt=len(medium2)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'medium/'+medium2[rand])
            medium2.pop(rand)
            cnt-=1
        except:
            pass       
    low1 = [file for file in os.listdir(train_dir+'low/') if 'Frontbumper' in file]
    low2 = [file for file in os.listdir(train_dir+'low/') if 'Rearbumper' in file]
    cnt=len(low1)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'low/'+low1[rand])
            low1.pop(rand)
            cnt-=1
        except:
            pass
    cnt=len(low2)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'low/'+low2[rand])
            low2.pop(rand)
            cnt-=1
        except:
            pass
       
    print("Done remove_custom")

def make_validset():
    if not os.path.exists(valid_dir):
        os.makedirs(valid_dir)
    if not os.path.exists(valid_dir+'high/'):
        os.makedirs(valid_dir+'high/')
    if not os.path.exists(valid_dir+'medium/'):
        os.makedirs(valid_dir+'medium/')
    if not os.path.exists(valid_dir+'low/'):
        os.makedirs(valid_dir+'low/')

    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    cnt=len(high)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'high/'+high[rand], valid_dir+'high/'+high[rand])
            high.pop(rand)
            cnt-=1
        except:
            pass
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    cnt=len(medium)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'medium/'+medium[rand], valid_dir+'medium/'+medium[rand])
            medium.pop(rand)
            cnt-=1
        except:
            pass
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    cnt=len(low)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'low/'+low[rand], valid_dir+'low/'+low[rand])
            low.pop(rand)
            cnt-=1
        except:
            pass

    print("Done make_validset")

def make_testset():
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    if not os.path.exists(test_dir+'high/'):
        os.makedirs(test_dir+'high/')
    if not os.path.exists(test_dir+'medium/'):
        os.makedirs(test_dir+'medium/')
    if not os.path.exists(test_dir+'low/'):
        os.makedirs(test_dir+'low/')

    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    cnt=len(high)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'high/'+high[rand], test_dir+'high/'+high[rand])
            high.pop(rand)
            cnt-=1
        except:
            pass
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    cnt=len(medium)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'medium/'+medium[rand], test_dir+'medium/'+medium[rand])
            medium.pop(rand)
            cnt-=1
        except:
            pass
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    cnt=len(low)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'low/'+low[rand], test_dir+'low/'+low[rand])
            low.pop(rand)
            cnt-=1
        except:
            pass

    print("Done make_testset")

#reset_dir()
#copy_to_train()
#confirm_train()
#remove_random()
#remove_custom()
#confirm_train()
#make_validset()
#make_testset()
confirm_train()
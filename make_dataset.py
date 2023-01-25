import os
import shutil
import random

data_dir = './data/img/'
train_dir = './data/train/'
valid_dir = './data/val/'
test_dir = './data/test/'

def copy_to_train():
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

def make_validset():
    if not os.path.exists(valid_dir+'high/'):
        os.makedirs(valid_dir+'high/')
    if not os.path.exists(valid_dir+'medium/'):
        os.makedirs(valid_dir+'medium/')
    if not os.path.exists(valid_dir+'low/'):
        os.makedirs(valid_dir+'low/')

    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    cnt=len(high)
    while cnt>6900:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'high/'+high[rand], valid_dir+'high/'+high[rand])
            high.pop(rand)
            cnt-=1
        except:
            pass
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    cnt=len(medium)
    while cnt>6900:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'medium/'+medium[rand], valid_dir+'medium/'+medium[rand])
            medium.pop(rand)
            cnt-=1
        except:
            pass
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    cnt=len(low)
    while cnt>6900:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'low/'+low[rand], valid_dir+'low/'+low[rand])
            low.pop(rand)
            cnt-=1
        except:
            pass

    print("Done make_validset")

def make_testset():
    if not os.path.exists(test_dir+'high/'):
        os.makedirs(test_dir+'high/')
    if not os.path.exists(test_dir+'medium/'):
        os.makedirs(test_dir+'medium/')
    if not os.path.exists(test_dir+'low/'):
        os.makedirs(test_dir+'low/')

    high = [file for file in os.listdir(train_dir+'high/') if file.endswith('.jpg')]
    cnt=len(high)
    while cnt>6200:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'high/'+high[rand], test_dir+'high/'+high[rand])
            high.pop(rand)
            cnt-=1
        except:
            pass
    medium = [file for file in os.listdir(train_dir+'medium/') if file.endswith('.jpg')]
    cnt=len(medium)
    while cnt>6200:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'medium/'+medium[rand], test_dir+'medium/'+medium[rand])
            medium.pop(rand)
            cnt-=1
        except:
            pass
    low = [file for file in os.listdir(train_dir+'low/') if file.endswith('.jpg')]
    cnt=len(low)
    while cnt>6200:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'low/'+low[rand], test_dir+'low/'+low[rand])
            low.pop(rand)
            cnt-=1
        except:
            pass

    print("Done make_testset")

copy_to_train()
remove_random()
make_validset()
make_testset()
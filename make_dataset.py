import os
import shutil
import random

data_dir = './data/img/'
train_dir = './data/train/'
valid_dir = './data/val/'
test_dir = './data/test/'

def reset_dir():
    if os.path.exists(train_dir+'detach/'):
        shutil.rmtree(train_dir+'detach')
        shutil.rmtree(train_dir+'oh')
        shutil.rmtree(train_dir+'overhall')
        shutil.rmtree(train_dir+'painting')
        shutil.rmtree(train_dir+'repair')
        shutil.rmtree(train_dir+'replace')
        shutil.rmtree(train_dir+'sheet')

    if os.path.exists(valid_dir+'detach/'):
        shutil.rmtree(valid_dir+'detach')
        shutil.rmtree(valid_dir+'oh')
        shutil.rmtree(valid_dir+'overhall')
        shutil.rmtree(valid_dir+'painting')
        shutil.rmtree(valid_dir+'repair')
        shutil.rmtree(valid_dir+'replace')
        shutil.rmtree(valid_dir+'sheet')

    if os.path.exists(test_dir+'detach/'):
        shutil.rmtree(test_dir+'detach')
        shutil.rmtree(test_dir+'oh')
        shutil.rmtree(test_dir+'overhall')
        shutil.rmtree(test_dir+'painting')
        shutil.rmtree(test_dir+'repair')
        shutil.rmtree(test_dir+'replace')
        shutil.rmtree(test_dir+'sheet')

def copy_to_train():
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(train_dir+'detach/'):
        os.makedirs(train_dir+'detach/')
    if not os.path.exists(train_dir+'oh/'):
        os.makedirs(train_dir+'oh/')
    if not os.path.exists(train_dir+'overhall/'):
        os.makedirs(train_dir+'overhall/')
    if not os.path.exists(train_dir+'painting/'):
        os.makedirs(train_dir+'painting/')
    if not os.path.exists(train_dir+'repair/'):
        os.makedirs(train_dir+'repair/')
    if not os.path.exists(train_dir+'replace/'):
        os.makedirs(train_dir+'replace/')
    if not os.path.exists(train_dir+'sheet/'):
        os.makedirs(train_dir+'sheet/')

    detach = [file for file in os.listdir(data_dir+'detach/') if file.endswith('.jpg')]
    for file in detach:
        shutil.copy(data_dir+'detach/'+file, train_dir+'detach/'+file)
    oh = [file for file in os.listdir(data_dir+'oh/') if file.endswith('.jpg')]
    for file in oh:
        shutil.copy(data_dir+'oh/'+file, train_dir+'oh/'+file)
    overhall = [file for file in os.listdir(data_dir+'overhall/') if file.endswith('.jpg')]
    for file in overhall:
        shutil.copy(data_dir+'overhall/'+file, train_dir+'overhall/'+file)
    painting = [file for file in os.listdir(data_dir+'painting/') if file.endswith('.jpg')]
    for file in painting:
        shutil.copy(data_dir+'painting/'+file, train_dir+'painting/'+file)
    repair = [file for file in os.listdir(data_dir+'repair/') if file.endswith('.jpg')]
    for file in repair:
        shutil.copy(data_dir+'repair/'+file, train_dir+'repair/'+file)
    replace = [file for file in os.listdir(data_dir+'replace/') if file.endswith('.jpg')]
    for file in replace:
        shutil.copy(data_dir+'replace/'+file, train_dir+'replace/'+file)
    sheet = [file for file in os.listdir(data_dir+'sheet/') if file.endswith('.jpg')]
    for file in sheet:
        shutil.copy(data_dir+'sheet/'+file, train_dir+'sheet/'+file)
    
    print("Done copy_to_train")

def confirm_train():
    detach_info={}
    detach = [file for file in os.listdir(train_dir+'detach/') if file.endswith('.jpg')]
    for file in detach:
        part = file.split('_')[2].replace('.jpg', '')
        if part in detach_info: detach_info[part]+=1
        else: detach_info[part]=1
    '''oh_info={}
    oh = [file for file in os.listdir(train_dir+'oh/') if file.endswith('.jpg')]
    for file in oh:
        part = file.split('_')[2].replace('.jpg', '')
        if part in oh_info: oh_info[part]+=1
        else: oh_info[part]=1'''
    overhall_info={}
    overhall = [file for file in os.listdir(train_dir+'overhall/') if file.endswith('.jpg')]
    for file in overhall:
        part = file.split('_')[2].replace('.jpg', '')
        if part in overhall_info: overhall_info[part]+=1
        else: overhall_info[part]=1
    '''painting_info={}
    painting = [file for file in os.listdir(train_dir+'painting/') if file.endswith('.jpg')]
    for file in painting:
        part = file.split('_')[2].replace('.jpg', '')
        if part in painting_info: painting_info[part]+=1
        else: painting_info[part]=1'''
    '''repair_info={}
    repair = [file for file in os.listdir(train_dir+'repair/') if file.endswith('.jpg')]
    for file in repair:
        part = file.split('_')[2].replace('.jpg', '')
        if part in repair_info: repair_info[part]+=1
        else: repair_info[part]=1'''
    replace_info={}
    replace = [file for file in os.listdir(train_dir+'replace/') if file.endswith('.jpg')]
    for file in replace:
        part = file.split('_')[2].replace('.jpg', '')
        if part in replace_info: replace_info[part]+=1
        else: replace_info[part]=1
    '''sheet_info={}
    sheet = [file for file in os.listdir(train_dir+'sheet/') if file.endswith('.jpg')]
    for file in sheet:
        part = file.split('_')[2].replace('.jpg', '')
        if part in sheet_info: sheet_info[part]+=1
        else: sheet_info[part]=1'''
    
    print("detach: ", detach_info, len(detach))
    #2OH:", oh_info, len(oh))
    print("overhall:", overhall_info, len(overhall))
    #print("painting:", painting_info, len(painting))
    #print("repair:", repair_info, len(repair))
    print("replace:", replace_info, len(replace))
    #print("sheet:", sheet_info, len(sheet))
    print("Done confirm_train")

def remove_custom():
    detach1 = [file for file in os.listdir(train_dir+'detach/') if 'Frontbumper' in file]
    detach2 = [file for file in os.listdir(train_dir+'detach/') if 'Rearbumper' in file]
    cnt=len(detach1)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'detach/'+detach1[rand]) 
            detach1.pop(rand)
            cnt-=1
        except:
            pass
    cnt=len(detach2)
    while cnt>1500:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'detach/'+detach2[rand]) 
            detach2.pop(rand)
            cnt-=1
        except:
            pass    
    
    detach = [file for file in os.listdir(train_dir+'detach/')]
    for file in detach:
        if file not in detach1 and file not in detach2: os.remove(train_dir+'detach/'+file)
     
    overhall1 = [file for file in os.listdir(train_dir+'overhall/') if 'Frontbumper' in file]
    overhall2 = [file for file in os.listdir(train_dir+'overhall/') if 'Rearbumper' in file]
    cnt=len(overhall1)
    while cnt>1600:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'overhall/'+overhall1[rand])
            overhall1.pop(rand)
            cnt-=1
        except:
            pass
    cnt=len(overhall2)
    while cnt>1600:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'overhall/'+overhall2[rand])
            overhall2.pop(rand)
            cnt-=1
        except:
            pass
        
    overhall = [file for file in os.listdir(train_dir+'overhall/')]
    for file in overhall:
        if file not in overhall1 and file not in overhall2: os.remove(train_dir+'overhall/'+file)
        
    replace1 = [file for file in os.listdir(train_dir+'replace/') if 'Frontbumper' in file]
    replace2 = [file for file in os.listdir(train_dir+'replace/') if 'Rearbumper' in file]
    cnt=len(replace1)
    while cnt>3200:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'replace/'+replace1[rand])
            replace1.pop(rand)
            cnt-=1
        except:
            pass
    cnt=len(replace2)
    while cnt>3200:
        rand = random.randrange(0,cnt)
        try:
            os.remove(train_dir+'replace/'+replace2[rand])
            replace2.pop(rand)
            cnt-=1
        except:
            pass
        
    replace = [file for file in os.listdir(train_dir+'replace/')]
    for file in replace:
        if file not in replace1 and file not in replace2: os.remove(train_dir+'replace/'+file)
       
    print("Done remove_custom")

def make_validset():
    if not os.path.exists(valid_dir):
        os.makedirs(valid_dir)
    if not os.path.exists(valid_dir+'detach/'):
        os.makedirs(valid_dir+'detach/')
    #if not os.path.exists(valid_dir+'oh/'):
    #    os.makedirs(valid_dir+'oh/')
    if not os.path.exists(valid_dir+'overhall/'):
        os.makedirs(valid_dir+'overhall/')
    #if not os.path.exists(valid_dir+'painting/'):
    #    os.makedirs(valid_dir+'painting/')
    #if not os.path.exists(valid_dir+'repair/'):
    #    os.makedirs(valid_dir+'repair/')
    if not os.path.exists(valid_dir+'replace/'):
        os.makedirs(valid_dir+'replace/')
    #if not os.path.exists(valid_dir+'sheet/'):
    #    os.makedirs(valid_dir+'sheet/')

    detach = [file for file in os.listdir(train_dir+'detach/') if file.endswith('.jpg')]
    cnt=len(detach)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'detach/'+detach[rand], valid_dir+'detach/'+detach[rand])
            detach.pop(rand)
            cnt-=1
        except:
            pass
    '''oh = [file for file in os.listdir(train_dir+'oh/') if file.endswith('.jpg')]
    cnt=len(oh)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'oh/'+oh[rand], valid_dir+'oh/'+oh[rand])
            oh.pop(rand)
            cnt-=1
        except:
            pass'''
    overhall = [file for file in os.listdir(train_dir+'overhall/') if file.endswith('.jpg')]
    cnt=len(overhall)
    while cnt>2900:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'overhall/'+overhall[rand], valid_dir+'overhall/'+overhall[rand])
            overhall.pop(rand)
            cnt-=1
        except:
            pass
    '''painting = [file for file in os.listdir(train_dir+'painting/') if file.endswith('.jpg')]
    cnt=len(painting)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'painting/'+painting[rand], valid_dir+'painting/'+painting[rand])
            painting.pop(rand)
            cnt-=1
        except:
            pass'''
    '''repair = [file for file in os.listdir(train_dir+'repair/') if file.endswith('.jpg')]
    cnt=len(repair)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'repair/'+repair[rand], valid_dir+'repair/'+repair[rand])
            repair.pop(rand)
            cnt-=1
        except:
            pass'''
    replace = [file for file in os.listdir(train_dir+'replace/') if file.endswith('.jpg')]
    cnt=len(replace)
    while cnt>5800:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'replace/'+replace[rand], valid_dir+'replace/'+replace[rand])
            replace.pop(rand)
            cnt-=1
        except:
            pass
    '''sheet = [file for file in os.listdir(train_dir+'sheet/') if file.endswith('.jpg')]
    cnt=len(sheet)
    while cnt>2700:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'sheet/'+sheet[rand], valid_dir+'sheet/'+sheet[rand])
            sheet.pop(rand)
            cnt-=1
        except:
            pass'''

    print("Done make_validset")

def make_testset():
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    if not os.path.exists(test_dir+'detach/'):
        os.makedirs(test_dir+'detach/')
    #if not os.path.exists(test_dir+'oh/'):
    #    os.makedirs(test_dir+'oh/')
    if not os.path.exists(test_dir+'overhall/'):
        os.makedirs(test_dir+'overhall/')
    #if not os.path.exists(test_dir+'painting/'):
    #    os.makedirs(test_dir+'painting/')
    #if not os.path.exists(test_dir+'repair/'):
    #    os.makedirs(test_dir+'repair/')
    if not os.path.exists(test_dir+'replace/'):
        os.makedirs(test_dir+'replace/')
    #if not os.path.exists(test_dir+'sheet/'):
    #    os.makedirs(test_dir+'sheet/')

    detach = [file for file in os.listdir(train_dir+'detach/') if file.endswith('.jpg')]
    cnt=len(detach)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'detach/'+detach[rand], test_dir+'detach/'+detach[rand])
            detach.pop(rand)
            cnt-=1
        except:
            pass
    '''oh = [file for file in os.listdir(train_dir+'oh/') if file.endswith('.jpg')]
    cnt=len(oh)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'oh/'+oh[rand], test_dir+'oh/'+oh[rand])
            oh.pop(rand)
            cnt-=1
        except:
            pass'''
    overhall = [file for file in os.listdir(train_dir+'overhall/') if file.endswith('.jpg')]
    cnt=len(overhall)
    while cnt>2600:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'overhall/'+overhall[rand], test_dir+'overhall/'+overhall[rand])
            overhall.pop(rand)
            cnt-=1
        except:
            pass
    '''painting = [file for file in os.listdir(train_dir+'painting/') if file.endswith('.jpg')]
    cnt=len(painting)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'painting/'+painting[rand], test_dir+'painting/'+painting[rand])
            painting.pop(rand)
            cnt-=1
        except:
            pass'''
    '''repair = [file for file in os.listdir(train_dir+'repair/') if file.endswith('.jpg')]
    cnt=len(repair)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'repair/'+repair[rand], test_dir+'repair/'+repair[rand])
            repair.pop(rand)
            cnt-=1
        except:
            pass'''
    replace = [file for file in os.listdir(train_dir+'replace/') if file.endswith('.jpg')]
    cnt=len(replace)
    while cnt>5200:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'replace/'+replace[rand], test_dir+'replace/'+replace[rand])
            replace.pop(rand)
            cnt-=1
        except:
            pass
    '''sheet = [file for file in os.listdir(train_dir+'sheet/') if file.endswith('.jpg')]
    cnt=len(sheet)
    while cnt>2400:
        rand = random.randrange(0,cnt)
        try:
            shutil.move(train_dir+'sheet/'+sheet[rand], test_dir+'sheet/'+sheet[rand])
            sheet.pop(rand)
            cnt-=1
        except:
            pass'''
    print("Done make_testset")

def confirm_valid():
    detach_info={}
    detach = [file for file in os.listdir(valid_dir+'detach/') if file.endswith('.jpg')]
    for file in detach:
        part = file.split('_')[2].replace('.jpg', '')
        if part in detach_info: detach_info[part]+=1
        else: detach_info[part]=1
    '''oh_info={}
    oh = [file for file in os.listdir(valid_dir+'oh/') if file.endswith('.jpg')]
    for file in oh:
        part = file.split('_')[2].replace('.jpg', '')
        if part in oh_info: oh_info[part]+=1
        else: oh_info[part]=1'''
    overhall_info={}
    overhall = [file for file in os.listdir(valid_dir+'overhall/') if file.endswith('.jpg')]
    for file in overhall:
        part = file.split('_')[2].replace('.jpg', '')
        if part in overhall_info: overhall_info[part]+=1
        else: overhall_info[part]=1
    '''painting_info={}
    painting = [file for file in os.listdir(valid_dir+'painting/') if file.endswith('.jpg')]
    for file in painting:
        part = file.split('_')[2].replace('.jpg', '')
        if part in painting_info: painting_info[part]+=1
        else: painting_info[part]=1'''
    '''repair_info={}
    repair = [file for file in os.listdir(valid_dir+'repair/') if file.endswith('.jpg')]
    for file in repair:
        part = file.split('_')[2].replace('.jpg', '')
        if part in repair_info: repair_info[part]+=1
        else: repair_info[part]=1'''
    replace_info={}
    replace = [file for file in os.listdir(valid_dir+'replace/') if file.endswith('.jpg')]
    for file in replace:
        part = file.split('_')[2].replace('.jpg', '')
        if part in replace_info: replace_info[part]+=1
        else: replace_info[part]=1
    '''sheet_info={}
    sheet = [file for file in os.listdir(valid_dir+'sheet/') if file.endswith('.jpg')]
    for file in sheet:
        part = file.split('_')[2].replace('.jpg', '')
        if part in sheet_info: sheet_info[part]+=1
        else: sheet_info[part]=1'''
    
    print("detach: ", detach_info, len(detach))
    #2OH:", oh_info, len(oh))
    print("overhall:", overhall_info, len(overhall))
    #print("painting:", painting_info, len(painting))
    #print("repair:", repair_info, len(repair))
    print("replace:", replace_info, len(replace))
    #print("sheet:", sheet_info, len(sheet))
    print("Done confirm_valid")

def confirm_test():
    detach_info={}
    detach = [file for file in os.listdir(test_dir+'detach/') if file.endswith('.jpg')]
    for file in detach:
        part = file.split('_')[2].replace('.jpg', '')
        if part in detach_info: detach_info[part]+=1
        else: detach_info[part]=1
    '''oh_info={}
    oh = [file for file in os.listdir(test_dir+'oh/') if file.endswith('.jpg')]
    for file in oh:
        part = file.split('_')[2].replace('.jpg', '')
        if part in oh_info: oh_info[part]+=1
        else: oh_info[part]=1'''
    overhall_info={}
    overhall = [file for file in os.listdir(test_dir+'overhall/') if file.endswith('.jpg')]
    for file in overhall:
        part = file.split('_')[2].replace('.jpg', '')
        if part in overhall_info: overhall_info[part]+=1
        else: overhall_info[part]=1
    '''painting_info={}
    painting = [file for file in os.listdir(test_dir+'painting/') if file.endswith('.jpg')]
    for file in painting:
        part = file.split('_')[2].replace('.jpg', '')
        if part in painting_info: painting_info[part]+=1
        else: painting_info[part]=1'''
    '''repair_info={}
    repair = [file for file in os.listdir(test_dir+'repair/') if file.endswith('.jpg')]
    for file in repair:
        part = file.split('_')[2].replace('.jpg', '')
        if part in repair_info: repair_info[part]+=1
        else: repair_info[part]=1'''
    replace_info={}
    replace = [file for file in os.listdir(test_dir+'replace/') if file.endswith('.jpg')]
    for file in replace:
        part = file.split('_')[2].replace('.jpg', '')
        if part in replace_info: replace_info[part]+=1
        else: replace_info[part]=1
    '''sheet_info={}
    sheet = [file for file in os.listdir(test_dir+'sheet/') if file.endswith('.jpg')]
    for file in sheet:
        part = file.split('_')[2].replace('.jpg', '')
        if part in sheet_info: sheet_info[part]+=1
        else: sheet_info[part]=1'''
    
    print("detach: ", detach_info, len(detach))
    #2OH:", oh_info, len(oh))
    print("overhall:", overhall_info, len(overhall))
    #print("painting:", painting_info, len(painting))
    #print("repair:", repair_info, len(repair))
    print("replace:", replace_info, len(replace))
    #print("sheet:", sheet_info, len(sheet))
    print("Done confirm_test")

    

#reset_dir()
#copy_to_train()
#confirm_train()
#remove_custom()
#confirm_train()
#make_validset()
#make_testset()
confirm_train()
confirm_valid()
confirm_test()
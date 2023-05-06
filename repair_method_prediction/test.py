import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models
from torchvision.models import VGG19_Weights
from torchvision.transforms import ToTensor
from PIL import Image
import pickle

test_dir = './data/test/'
REPAIR_METHOD_WEIGHT = './data/weight/repair_method_vgg19.pth'
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

modelvgg = models.vgg19(weights=VGG19_Weights.DEFAULT) # vgg 19

#class 0: detach
#class 1: overhall
#class 2: replace
def get_class(model, origImage):
    tf_toTensor = ToTensor()
    image = tf_toTensor(origImage).float().to(DEVICE)
    
    predictions = model(image.unsqueeze(0))
    prediction = predictions[0].detach().cpu()
    cl = np.argmax(prediction)

    return int(cl)

# Create base class
class ImageClassificationBase(nn.Module):
    def training_step(self, batch):
        images, labels = batch 
        out = self(images)                  # Generate predictions
        loss = F.cross_entropy(out, labels) # Calculate loss
        return loss
    
    def validation_step(self, batch):
        images, labels = batch 
        out = self(images)                    # Generate predictions
        loss = F.cross_entropy(out, labels)   # Calculate loss
        acc = accuracy(out, labels)           # Calculate accuracy
        return {'val_loss': loss.detach(), 'val_acc': acc}
        
    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()   # Combine losses
        batch_accs = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_accs).mean()      # Combine accuracies
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
    def epoch_end(self, epoch, result):
        print("Epoch [{}], train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
            epoch, result['train_loss'], result['val_loss'], result['val_acc']))

#Inherit base class
class IntelCnnModel(ImageClassificationBase) :
    def __init__(self) :
        super().__init__()
        self.network = modelvgg
        #self.network = torch.load("./modelvgg_intel.pth")
    def forward(self, xb) :
        return self.network(xb)

# Create object of inherited class
model = IntelCnnModel() # vgg19 model
model = torch.load(REPAIR_METHOD_WEIGHT)

cnt_detach=0
cnt_overhall=0
cnt_replace=0

part1_wrong=0
part2_wrong=0

detach_wrong_list=[]
overhall_wrong_list=[]
replace_wrong_list=[]

detach = [file for file in os.listdir(test_dir+'detach/') if file.endswith('.jpg')]
for f in detach:
    file = test_dir+'detach/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    cl = get_class(model, image)
    if cl == 0: 
        cnt_detach+=1
    else:
        detach_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

#print('Wrong in detach:')
#print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_detach) * 100, 2),"%")
#print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_detach) * 100, 2),"%")

part1_wrong=0
part2_wrong=0

overhall = [file for file in os.listdir(test_dir+'overhall/') if file.endswith('.jpg')]
for f in overhall:
    file = test_dir+'overhall/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    cl = get_class(model, image)
    if cl == 1: cnt_overhall+=1
    else:
        overhall_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

#print('Wrong in overhall:')
#print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_overhall) * 100, 2),"%")
#print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_overhall) * 100, 2),"%")

part1_wrong=0
part2_wrong=0

replace = [file for file in os.listdir(test_dir+'replace/') if file.endswith('.jpg')]
for f in replace:
    file = test_dir+'replace/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    cl = get_class(model, image)
    if cl == 2: cnt_replace+=1
    else:
        replace_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

#print('Wrong in replace:')
#print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_replace) * 100, 2),"%")
#print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_replace) * 100, 2),"%")

print()

print("accuracy of detach:",round(cnt_detach/600 * 100, 2),"%")
print("accuracy of overhall:",round(cnt_overhall/400 * 100, 2),"%")
print("accuracy of replace:",round(cnt_replace/1500 * 100, 2),"%")

#with open('./data/datainfo/detach_wrong_list.txt', 'w') as f:
#    for item in detach_wrong_list:
#        f.write(item+'\n')

#with open('./data/datainfo/overhall_wrong_list.txt', 'w') as f:
#    for item in overhall_wrong_list:
#        f.write(item+'\n')

#with open('./data/datainfo/replace_wrong_list.txt', 'w') as f:
#    for item in replace_wrong_list:
#        f.write(item+'\n')



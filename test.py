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
SEVERITY_WEIGHT = './data/weight/severityVGG19.pth'
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

modelvgg = models.vgg19(weights=VGG19_Weights.DEFAULT) # vgg 19

#class 0: High
#class 1: Low
#class 2: Medium
def get_class(model, origImage):
    tf_toTensor = ToTensor()
    image = tf_toTensor(origImage).float().to(DEVICE)
    
    predictions = model(image.unsqueeze(0))
    prediction = predictions[0].detach().cpu()
    severity = np.argmax(prediction)

    return severity

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
model = torch.load(SEVERITY_WEIGHT)

cnt_high=0
cnt_medium=0
cnt_low=0

part1_wrong=0
part2_wrong=0

high_wrong_list=[]
medium_wrong_list=[]
low_wrong_list=[]

high = [file for file in os.listdir(test_dir+'high/') if file.endswith('.jpg')]
for f in high:
    file = test_dir+'high/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 0: 
        cnt_high+=1
    else:
        high_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

print('Wrong in High:')
print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_high) * 100, 2),"%")
print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_high) * 100, 2),"%")

part1_wrong=0
part2_wrong=0

medium = [file for file in os.listdir(test_dir+'medium/') if file.endswith('.jpg')]
for f in medium:
    file = test_dir+'medium/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 2: cnt_medium+=1
    else:
        medium_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

print('Wrong in Medium:')
print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_medium) * 100, 2),"%")
print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_medium) * 100, 2),"%")

part1_wrong=0
part2_wrong=0

low = [file for file in os.listdir(test_dir+'low/') if file.endswith('.jpg')]
for f in low:
    file = test_dir+'low/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 1: cnt_low+=1
    else:
        low_wrong_list.append(file)
        if 'Frontbumper' in file: part1_wrong+=1
        else: part2_wrong+=1

print('Wrong in Low:')
print('Frontbumper Wrong: ', round(part1_wrong/(300-cnt_low) * 100, 2),"%")
print('Rearbumper Wrong: ', round(part2_wrong/(300-cnt_low) * 100, 2),"%")

print()

print("accuracy of high:",round(cnt_high/200 * 100, 2),"%")
print("accuracy of medium:",round(cnt_medium/200 * 100, 2),"%")
print("accuracy of low:",round(cnt_low/200 * 100, 2),"%")

with open('./data/datainfo/high_wrong_list.txt', 'w') as f:
    for item in high_wrong_list:
        f.write(item+'\n')

with open('./data/datainfo/medium_wrong_list.txt', 'w') as f:
    for item in medium_wrong_list:
        f.write(item+'\n')

with open('./data/datainfo/low_wrong_list.txt', 'w') as f:
    for item in low_wrong_list:
        f.write(item+'\n')



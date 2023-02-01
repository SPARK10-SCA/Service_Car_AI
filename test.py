import os
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models
from torchvision.models import VGG19_Weights
from torchvision.transforms import ToTensor
from PIL import Image

test_dir = './data2/test/'
SEVERITY_WEIGHT = './data2/weight/severityVGG19.pth'
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

cnt=0
high = [file for file in os.listdir(test_dir+'high/') if file.endswith('.jpg')]
for f in high:
    file = test_dir+'high/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 0: cnt+=1
medium = [file for file in os.listdir(test_dir+'medium/') if file.endswith('.jpg')]
for f in medium:
    file = test_dir+'medium/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 2: cnt+=1
low = [file for file in os.listdir(test_dir+'low/') if file.endswith('.jpg')]
for f in low:
    file = test_dir+'low/'+f
    image = Image.open(file)
    image = image.resize((224,224))
    severity = int(get_class(model, image))
    if severity == 1: cnt+=1

print("accuracy:",round(cnt/2100 * 100, 2),"%")



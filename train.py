import os
import torch
import tarfile
import torchvision
import torch.nn as nn
from PIL import Image
import matplotlib.pyplot as plt
import torch.nn.functional as F
from torchvision import transforms
from torchvision.utils import make_grid
from torch.utils.data import random_split
from torchvision.transforms import ToTensor
from torchvision.datasets import ImageFolder
from torch.utils.data import Dataset, DataLoader
from torchvision.datasets.utils import download_url
import pathlib # path에 있는 폴더 이름 가져오기
import numpy as np
from torchvision import models
from torchvision.models import VGG19_Weights
import pickle


transform_train = transforms.Compose([
    transforms.Resize((224,224)), #becasue vgg takes 150*150
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((.5, .5, .5), (.5, .5, .5))
])

#Augmentation is not done for test/validation data.
transform_test = transforms.Compose([
    transforms.Resize((224,224)), #becasue vgg takes 150*150
    transforms.ToTensor(),
    transforms.Normalize((.5, .5, .5), (.5, .5, .5))
])

# 이미지 가져오기 (폴더로 나눠주면 알아서 labeling 해준다 )
train_ds = ImageFolder('/home/work/hyunbin/severity/data/train/', transform=transform_train)
val_ds = ImageFolder('/home/work/hyunbin/severity/data/val/', transform=transform_test)

batch_size=32
train_dl = DataLoader(train_ds, batch_size, shuffle=True, num_workers=4, pin_memory=True)
val_dl = DataLoader(val_ds, batch_size, num_workers=4, pin_memory=True)

# path에 있는 폴더이름으로 class name 만들기
root = pathlib.Path("/home/work/hyunbin/severity/data/train/")
classes = sorted([j.name.split('/')[-1] for j in root.iterdir()])
print(classes)

modelvgg = models.vgg19(weights=VGG19_Weights.DEFAULT) # vgg 19

for p in modelvgg.parameters() : # layers freeze
    p.requires_grad = False

modelvgg.classifier = nn.Sequential(
    nn.Linear(in_features=25088, out_features=2048),
    nn.ReLU(),
    nn.Linear(in_features=2048, out_features=512),
    nn.ReLU(),
    nn.Dropout(p=0.6),
    nn.Linear(in_features=512,out_features=3), # class 3개로 설정
    nn.LogSoftmax(dim=1)
)

# accuracy function 만들기
def accuracy(outputs, labels) :
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))

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

# Check device
def get_default_device() :
    if torch.cuda.is_available() :
        print("gpu 인식 성공")
        return torch.device('cuda')
    else :
        print("gpu 인식 실패")
        return torch.device('cpu')

device = get_default_device()

def to_device(data, device) :
    if isinstance(data, (list,tuple)) :
        return [to_device(x,device) for x in data]
    return data.to(device, non_blocking = True)

def evaluate(model, val_loader):
    model.eval()   #eval() is called to tell model that now it is validation mode and so don't perform stuff like dropout,backpropagation etc..
    outputs = [model.validation_step(batch) for batch in val_loader]
    return model.validation_epoch_end(outputs)

def fit(epochs, lr, model, train_loader, val_loader, opt_func=torch.optim.Adam):
    history = []
    optimizer = opt_func(model.parameters(), lr)
    for epoch in range(epochs):
        # Training Phase 
        model.train() #eval() is called to tell model that now it is training mode and so  perform stuff like dropout,backpropagation etc..
        train_losses = []
        for batch in train_loader:
            loss = model.training_step(batch)
            train_losses.append(loss)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
        # Validation phase
        result = evaluate(model, val_loader)
        result['train_loss'] = torch.stack(train_losses).mean().item()
        model.epoch_end(epoch, result)
        history.append(result)
    return history

class DeviceDataLoader():
    """Wrap a dataloader to move data to a device"""
    def __init__(self, dl, device):
        self.dl = dl
        self.device = device
        
    def __iter__(self):
        """Yield a batch of data after moving it to device"""
        for b in self.dl: 
            yield to_device(b, self.device)

    def __len__(self):
        """Number of batches"""
        return len(self.dl)

# 이미지 넣어서 label 값 예측하기
def predict_single(input, label, model):
    input = to_device(input,device)
    inputs = input.unsqueeze(0)   # unsqueeze the input i.e. add an additonal dimension
    predictions = model(inputs)
    prediction = predictions[0].detach().cpu()
    print(f"Prediction is {np.argmax(prediction)} of Model whereas given label is {label}")

def train_model(model) :
    num_epochs = 128
    opt_func = torch.optim.Adam
    lr = 0.00001
    history = fit(num_epochs, lr, model, train_dl, val_dl, opt_func)

    with open('/home/work/hyunbin/severity/data/weight/vgg_trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history, file_pi)


train_dl = DeviceDataLoader(train_dl, device) 
val_dl = DeviceDataLoader(val_dl, device)

model = to_device(model, device) # vgg19 model

train_model(model)
torch.save(model, '/home/work/hyunbin/severity/data/weight/severityVGG19.pth')
val = evaluate(model, val_dl)

#print("model validation : ",val)
#for i,img in enumerate(val_ds):
#    predict_single(img[0],img[1],model)
    
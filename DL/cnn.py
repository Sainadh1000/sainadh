import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

a=480

class simpleCnn(nn.Module):
  def __init__(self,num_classes):
    super(simpleCnn,self).__init__()
    self.conv1=nn.Conv2d(
        in_channels=1,
        out_channels=16,
        kernel_size=3,
        padding=1,
        stride=1
    )
    self.conv2=nn.Conv2d(
        in_channels=16,
        out_channels=16,
        kernel_size=3,
        padding=1,
        stride=1
    )
    self.conv3=nn.Conv2d(
        in_channels=16,
        out_channels=16,
        kernel_size=3,
        padding=1,
        stride=1
    )

    self.pool=nn.MaxPool2d(2,2)
    self.fc1=nn.Linear(16*60*60,128)
    self.fc2=nn.Linear(128,128)
    self.out=nn.Linear(128,num_classes)

  def forward(self,x):
    x=self.pool(self.conv1(x))
    x=self.pool(self.conv2(x))
    x=self.pool(self.conv3(x))
    x=torch.flatten(x,start_dim=1)
    x=F.relu(self.fc1(x))
    x=F.relu(self.fc2(x))
    x=self.out(x)
    return x
  

model=simpleCnn(num_classes=10)

x= torch.randn(10,1,a,a)  # creates 10 random grayscale images with size a*a
y=model(x)

print(y)


criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr=0.001)
y=model(x)

print(y)
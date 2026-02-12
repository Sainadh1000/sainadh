import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

x,y=make_moons(n_samples=200,noise=0.2,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
x_train=torch.tensor(x_train,dtype=torch.float32)
x_test=torch.tensor(x_test,dtype=torch.float32)
y_train=torch.tensor(y_train,dtype=torch.float32).unsqueeze(1)
y_test=torch.tensor(y_test,dtype=torch.float32).unsqueeze(1)

class simpleANN(nn.Module):
  def __init__(self):
    super(simpleANN,self).__init__()
    self.hidden1=nn.Linear(2,8)
    self.hidden2=nn.Linear(8,8)
    self.hidden3=nn.Linear(8,8)
    self.out=nn.Linear(8,1)
    self.relu=nn.ReLU()
    self.sigmoid=nn.Sigmoid()
  def forward(self,x):
    x=self.relu(self.hidden1(x))
    x=self.relu(self.hidden2(x))
    x=self.relu(self.hidden3(x))
    x=self.sigmoid(self.out(x))
    return x

model=simpleANN()
criterion=nn.BCELoss()
optimizer=optim.Adam(model.parameters(),lr=0.03)

losses=[]



for epoch in range(200):
  y_pred=model(x_train)
  loss=criterion(y_pred,y_train)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  losses.append(loss.item())

with torch.no_grad():
    y_test_pred = model(x_test)
    predicted_test = (y_test_pred >= 0.5).float()
    correct_test = (predicted_test == y_test).sum().item()
    test_accuracy = correct_test / y_test.size(0)

print(f"Test Accuracy: {test_accuracy * 100:.2f}%")


plt.plot(losses)
plt.xlabel("Epoches")
plt.ylabel("loss")
plt.title("Training loss(Py Torch)")
plt.show()

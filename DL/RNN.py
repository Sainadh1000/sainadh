import torch
import torch.nn as nn

class simpleRNN(nn.Module):
  def __init__(self,input_size,hidden_size,num_layers,num_classes):
    super(simpleRNN,self).__init__()
    self.hidden_size=hidden_size
    self.num_layers=num_layers

    self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
    self.fc=nn.Linear(hidden_size,num_classes)

  def forward(self,x):
    h0=torch.zeros(self.num_layers,x.size(0),self.hidden_size)
    out,_=self.rnn(x,h0)
    out=self.fc(out[:,-1,:])
    return out

input_size = 1
hidden_size = 28
num_layers = 2
num_classes = 2
seq_len = 10
batch_size = 16

model=simpleRNN(input_size,hidden_size,num_layers,num_classes)
criterion = nn.CrossEntropyLoss()
optimizer= torch.optim.Adam(model.parameters(),lr=0.001)

x=torch.randn(batch_size,seq_len,input_size)
y=torch.randint(0,2,(batch_size,))
# training step
outputs = model(X)
loss = criterion(outputs, y)

optimizer.zero_grad()
loss.backward()
optimizer.step()

print("Loss:", loss.item())



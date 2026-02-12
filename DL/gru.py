import torch
import torch.nn as nn

class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(SimpleGRU, self).__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )

        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # x: (batch, seq_len, input_size)

        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size, device=x.device)

        out, hn = self.gru(x, h0)
        # out: (batch, seq_len, hidden_size)

        last_out = out[:, -1, :]   # last time step

        out = self.fc(last_out)
        return out
    
input_size = 1
hidden_size = 32
num_layers = 1
num_classes = 2
seq_len = 10
batch_size = 16
model = SimpleGRU(input_size, hidden_size, num_layers, num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

X = torch.randn(batch_size, seq_len, input_size)
y = torch.randint(0, num_classes, (batch_size,))

outputs = model(X)
loss = criterion(outputs, y)

optimizer.zero_grad()
loss.backward()
optimizer.step()

print("Loss:", loss.item())
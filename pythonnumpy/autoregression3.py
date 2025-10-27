inputs= [
251.12, 249.78, 254.64, 257.31, 255.02,
253.48, 252.11, 250.85, 254.23, 256.14,
248.97, 243.46, 244.28, 246.01, 248.93,
251.47, 249.82, 248.76, 251.36, 252.89
]
past=inputs[:-1]
present=inputs[1:]
import numpy as np
ones=np.ones(len(past))
x=np.c_[ones,past]
y=np.c_[present]

def weights(x,y):
    from numpy.linalg import inv
    l=inv(x.T.dot(x))
    r=x.T.dot(y)
    return l.dot(r)
w=weights(x,y)
ycap=x.dot(w)
def accuracy(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    acc=(1-(rss/tss))*100
    return acc
efficiency=accuracy(y,ycap)
print(efficiency)
p=np.array([[1,inputs[-1]]])
tommorow=p.dot(w)
print(f"tommorow inputs:{tommorow}")
infile= open('./pythonnumpy/pdia.txt')
header=infile.readline()
data=infile.readlines()
inputs = []
dstat = []
for line in data:
   w = line.strip().lower().split(',')
   ins =[float(v) for v in  w[:-1]]
   inputs.append(ins)
   d = w[-1]
   if d=='yes':
     dstat.append(1)
   else:
     dstat.append(0)
print(inputs)

import numpy as np
ones=np.ones(len(data))
x=np.c_[ones,inputs]
y=np.c_[dstat]
def weights(x,y):
    from numpy.linalg import inv
    left=inv((x).T.dot(x))
    right=x.T.dot(y)
    return left.dot(right)
def predict(x, w):
   return 1/(1+np.exp(-x.dot(w)))
w=weights(x,y)
print(w)
ypred=predict(x,w)
print(ypred)
ycap = np.where(ypred>0.5, 1 , 0)
ycap
def efficiency(y, ycap):
   pcnt = np.where(y == ycap)[0].size
   n = len(y)
   acc = pcnt/n * 100
   return acc
print(efficiency(y, ycap))

def  poly(x, degree):
    x = x[:,1: ]  # 5
    m = []
    for c in range(x.shape[1]):
       for i in range(degree):
         col = x[:, c]**(i+1)
         m.append(col)
    m = np.array(m)
    m = m.T
    o = np.ones(x.shape[0])
    M = np.c_[o, m]
    return M
X2 = poly(x, 2)
X3 = poly(x, 3)
X4 = poly(x, 4)
print(x.shape) 
print(X2.shape)
print(X3.shape)
print(X4.shape)

W2 = weights(X2, y)
ypred2 = predict(X2, W2 )
ycap2 = np.where(ypred2>0.5, 1, 0)
eff2 = efficiency(y, ycap2)
print(eff2)

W3 = weights(X3, y)
ypred3 = predict(X3, W3 )
ycap3= np.where(ypred3>0.5, 1, 0)
eff3 = efficiency(y, ycap3)
print(eff3)

W4= weights(X4, y)
ypred4 = predict(X4, W4 )
ycap4= np.where(ypred4>0.5, 1, 0)
eff4 = efficiency(y, ycap4)
print(eff4)
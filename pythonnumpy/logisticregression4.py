infile=open('./pythonnumpy/pdia.txt')
header=infile.readline()
data=infile.readlines()
inputs=[]
outputs=[]
for line in data:
    w=line.strip().lower().split(',')
    ins=[float(x) for x in w[:-1]]
    inputs.append(ins)
    if w[-1]=='yes':
        outputs.append(1)
    else:
        outputs.append(0)
import numpy as np
ones=np.ones(len(inputs))
x=np.c_[ones,inputs]
y=np.c_[outputs]

def weights(x,y):
    from numpy.linalg import inv
    l=inv(x.T.dot(x))
    r=x.T.dot(y)
    return l.dot(r)
def predict(x,w):
    return 1/(1+np.exp(-x.dot(w)))
w=weights(x,y)
ypred=predict(x,w)
ycap=np.where(ypred>0.5,1,0)
def accuracy(y,ycap):
    pnct=np.where(y==ycap)[0].size
    n=len(y)
    return (pnct/n)*100
print(accuracy(y,ycap))

def poly(x, degree):
    x = x[:,1: ] 
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
x2=poly(x,2)
w2=weights(x2,y)
ypred2=predict(x2,w2)
ycap2=np.where(ypred2>0.5,1,0)
accuracy2=accuracy(y,ycap2)
print(accuracy2)

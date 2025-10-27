import numpy as np
infile=open('./pythonnumpy/pdia2.txt')
header=infile.readline()
data=infile.readlines()
inputs=[]
outputs=[]
for line in data:
    w=line.strip().lower().split(',')
    i=[float(x)  for x in w[:-1]]
    inputs.append(i)
    if w[-1]=='yes':
        outputs.append(1)
    else:
        outputs.append(0)
print(inputs)
print(outputs)
ones=np.ones(len(inputs))
x=np.c_[ones,inputs]
y=np.c_[outputs]
def weights(x,y):
    from numpy.linalg import inv
    l=inv(x.T.dot(x))
    r=x.T.dot(y)
    return l.dot(r)
def predict(x, w):
   return 1/(1+np.exp(-x.dot(w)))
w=weights(x,y)
print(w)
ypred=predict(x,w)
print(ypred)
ycap=np.where(ypred>0.5,1,0)
print(ycap)
def accuracy(y,ycap):
    pnct=np.where(y==ycap)[0].size
    n=len(y)
    return (pnct/n)*100
print(accuracy(y,ycap))

def poly(x,degree):
    x=x[:,1:]
    m=[]
    for c in range(x.shape[1]):
        for i in range(degree):
            col=x[:,c]**(i+1)
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
x3=poly(x,3)
w3=weights(x3,y)
ypred3=predict(x3,w3)
ycap3=np.where(ypred3>0.5,1,0)
accuracy3=accuracy(y,ycap3)
print(accuracy3)

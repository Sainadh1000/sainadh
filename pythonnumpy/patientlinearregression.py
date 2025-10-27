inputdata=open('./pythonnumpy/patientfile.txt')
header=inputdata.readline()
numericdata=inputdata.readlines()
data=[]
for i in numericdata:
    data.append(i.strip().split(','))
inputs = [row[:3] for row in data]
def tofloat(xlist):
    return[float(x) for x in xlist]
inputs=[tofloat(row[:3]) for row in data]   
outputs=[float(x[-1]) for x in data]
import numpy as np
ones=np.ones(len(inputs))
x=np.c_[ones,inputs]
y=np.c_[outputs]
def weights(x,y):
    from numpy.linalg import inv
    lef=inv(x.T.dot(x))
    rgt=x.T.dot(y)
    return lef.dot(rgt)
w=weights(x,y)
print(w)

ycap=x.dot(w)
print(ycap)
print(np.c_[y,ycap])

def accuracy(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    acc=(1-(rss/tss))*100
    return acc
model_accuracy=accuracy(y,ycap)
print(model_accuracy)
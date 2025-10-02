data=open('./pythonnumpy/diabaticdata.txt')
header=data.readline()
numericdata=data.readlines()
dataframe=[]
for line in numericdata:
    dataframe.append(line.strip().split(','))
    print(dataframe)
indata=[row[:3] for row in dataframe]
def tofloat(xlist):
    return [float(x) for x in xlist]
indata=[tofloat(i) for i in indata]
print(indata)
outdata=[float(row[-1]) for row in dataframe]
print(outdata)

import numpy as np
ones=np.ones(len(dataframe))
x=np.c_[ones,indata]
print(x)
y=np.c_[outdata]
print(y)
def weights(x,y):
    from numpy.linalg import inv
    left=inv(x.T.dot(x))
    right=x.T.dot(y)
    return left.dot(right)
w=weights(x,y)
ycap = x.dot(w)
def efficiency(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    rs = 1 - (rss/tss)
    return rs
rs=efficiency(y,ycap)
isefficient=accuracy = rs * 100
print("Accuracy of model ", isefficient)



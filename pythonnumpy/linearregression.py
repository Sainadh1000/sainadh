data = open('./pythonnumpy/diabaticdata.txt')
header = data.readline()
numericdata = data.readlines()
print("Header:", header)
print("Raw data lines:", numericdata)
datawords = []
for line in numericdata:
    datawords.append(line.strip().split(','))
inputs = [row[:3] for row in datawords]
def tofloat(xlist):
    return [float(x) for x in xlist]
inputs = [tofloat(i) for i in inputs]
print("Numeric Inputs:",inputs)
dscore=[float(x[-1]) for x in datawords]
print(dscore)

import numpy as np
ones=np.ones(len(datawords))
x=np.c_[ones,inputs]
print(x)

y=np.c_[dscore]
print(y)

def weights(x,y):
   from numpy.linalg import inv
   left = inv(x.T.dot(x))
   rgt = x.T.dot(y)
   return left.dot(rgt)
w= weights(x, y)
print(w.shape)
print(w)
ycap = x.dot(w)
print(ycap.shape)

compare=np.c_[y,ycap]
print(compare)

def efficiency(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    rs = 1 - (rss/tss)
    return rs
rs=efficiency(y,ycap)
isefficient=accuracy = rs * 100
print("Accuracy of model ", isefficient)
print(dscore)
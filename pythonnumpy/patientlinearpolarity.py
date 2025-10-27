import numpy as np
inputdata=open('./pythonnumpy/patientfile.txt')
header=inputdata.readline()
numdata=inputdata.readlines()
gl=[]
ins=[]
bp=[]
dscore=[]
for i in numdata:
    puredata=i.strip().split(',')
    gl.append(float(puredata[0]))
    ins.append(float(puredata[1]))
    bp.append(float(puredata[2]))
    dscore.append(float(puredata[3]))
ones=np.ones(len(gl))
x=np.c_[ones,gl,ins,bp]
y=np.c_[dscore]
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
    return (1-(rss/tss))
model_accuracy=accuracy(y,ycap)*100
print(model_accuracy)
gl = np.array(gl)
ins = np.array(ins)
bp = np.array(bp)
dscore = np.array(dscore)
gl2=gl**2
ins2=ins**2
bp2=bp**2
x2=np.c_[ones,gl,gl2,ins,ins2,bp,bp2]
w2=weights(x2,y)
ycap2=x2.dot(w2)
model_accuracy2=accuracy(y,ycap2)*100
print(model_accuracy2)
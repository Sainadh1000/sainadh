infile=open('./pythonnumpy/diabaticdata.txt')
header=infile.readline()
data=infile.readlines()
gl=[]
ins=[]
bp=[]
dscore=[]
for i in data:
    w=i.strip().split(',')
    gl.append(float(w[0]))
    ins.append(float(w[1]))
    bp.append(float(w[2]))
    dscore.append(float(w[-1]))
import numpy as np
gl = np.array(gl)
ins = np.array(ins)
bp = np.array(bp)
dscore = np.array(dscore)
ones=np.ones(len(gl))
x=np.c_[ones,gl,ins,bp]
y=np.c_[dscore]
print(x)
print(y)
def weights(x,y):
    from numpy.linalg import inv
    left=inv((x).T.dot(x))
    right=x.T.dot(y)
    return left.dot(right)
w=weights(x,y)
print(w)
ycap=x.dot(w)
def accuracy(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    rs=1-(rss/tss)
    return rs
efficiency=accuracy(y,ycap)*100
print(efficiency)

gl2=gl**2
ins2=ins**2
bp2=bp**2
x_poly2=np.c_[ones,gl,gl2,ins,ins2,bp,bp2]
w_poly2=weights(x_poly2,y)
print(w_poly2)
y_poly2=x_poly2.dot(w_poly2)
print(y_poly2)
efficiency_poly2=accuracy(y,y_poly2)*100
print(efficiency_poly2)
wipro = [249.63, 250.33, 255.88, 256.93, 254.15,254.01, 251.28, 251.94, 253.91, 255.75,249.15, 242.52, 243.67, 244.97, 249.56,250.93, 250.36, 249.41, 250.65, 252.03]
past=wipro[:-1]
present=wipro[1:]
import numpy as np
print(np.corrcoef(past, present))
ones=np.ones(len(past))
x=np.c_[ones,past]
print(x)
y=np.c_[present]
print(y)

def weights(x,y):
    from numpy.linalg import inv
    l=inv(x.T.dot(x))
    r=x.T.dot(y)
    return l.dot(r)
w=weights(x,y)
print(w)

ycap=x.dot(w)
print(ycap)

def rsquare(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    rs=1-(rss/tss)
    return rs
accuracy=rsquare(y,ycap)*100
print(accuracy)

p=np.array(past)
p2=p**2
x2=np.c_[ones,p,p2]
w2=weights(x2,y)
print(w2)
ycap2=x2.dot(w2)
accuracy2=rsquare(y,ycap2)*100
print(accuracy2)
print(f"model is not efficient with success rate of {accuracy2} add another polynomial degree")


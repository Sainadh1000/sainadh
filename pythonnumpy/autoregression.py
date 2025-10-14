temp=[10, 12, 13, 14.5, 16, 17, 17.9, 18, 21, 22, 21, 20, 18.7, 18, 16.8, 16, 15.4, 15.1]
past=temp[:-1]
present=temp[1:]
import numpy as np
ones=np.ones(len(past))
x=np.c_[ones,past]
print(x)
y=np.c_[present]
def weights(x,y):
    from numpy.linalg import inv
    lef=inv(x.T.dot(x))
    rgh=x.T.dot(y)
    return lef.dot(rgh)
w=weights(x,y)
print(w)
ycap=x.dot(w)
print(ycap)

def rsquare(y, ycap):
  rss =  ((y-ycap)**2).sum()
  tss =  ((y-y.mean())**2).sum()
  rs = 1-(rss/tss)
  return rs
accuracy=rsquare(y,ycap)*100
print(accuracy)

P = np.array([[1, temp[-1] ]])
print(P)
tommorow=P.dot(w)
print(tommorow)
print(f"tommorow temparature is:{tommorow}")
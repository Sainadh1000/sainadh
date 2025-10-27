import numpy as np
icecream = [33.49, 37.15, 34.05, 31.44, 24.91, 40.06, 41.27, 43.83, 26.78, 29.14]
icecream=np.array(icecream)
temp=1.5*icecream
ones=np.ones(len(icecream))
x=np.c_[ones,icecream]
y=np.c_[temp]

def scale(x):
    x=np.array(x)
    return (x-x.mean())/x.std()
icecream_scale=scale(icecream)
x_scale=np.c_[ones,icecream_scale]
y_scale=scale(y)

np.random.seed(100)
w=np.random.random ((x.shape[1],1))*2-1


convergence=0.0000001
flag=0
ploss=0
for i in range(10000):
    ycap=x_scale.dot(w)
    closs=((y_scale-ycap)**2).mean()
    delta=x_scale.T.dot(y_scale-ycap)/y_scale.shape[0]
    if i%100==0:
        print("current loss:",closs)
    w=delta*0.2
    if np.abs(ploss-closs)<=convergence:
        print(f"training completed after {i+1} iterations")
        flag=1
        break
    ploss=closs
if flag==0:
    print("training not completed run few more iterations")
def accuracy(y,ycap):
    rss=((y-ycap)**2).sum()
    tss=((y-y.mean())**2).sum()
    rsquare=1-(rss/tss)
    return rsquare*100
model_efficiency=accuracy(y_scale,ycap)
print(model_efficiency)

ypred=y.std()*y_scale+y.mean()
print(ypred)
print(np.c_[y,ypred])
print(accuracy(y,ypred))



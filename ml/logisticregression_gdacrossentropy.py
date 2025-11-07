import numpy as np
import pandas as pd
df=pd.read_csv('ml/textfile.txt')
df.info()
inputsdf=df.iloc[:,:-2]
inputs=inputsdf.to_numpy()
print(inputs)

dstat = df['Diabetic Status']
print(dstat)
dh=np.where(dstat=='Yes', 1, 0)



def scale(x):
    return (x-x.mean())/x.std()
def scaleMatrix(x):
   for i in range(x.shape[1]):
      x[:, i] = scale(x[:, i])
   return x
inputs_scaled = scaleMatrix(inputs)


ones=np.ones(inputs.shape[0])
X=np.c_[ones,inputs_scaled]
Y=np.c_[dh]

def prediction(x,w):
   return 1 / (1 + np.exp(-x.dot(w)))

def derivative(p):
   return p * (1 - p)
np.random.seed(101)
W = np.random.random((X.shape[1], Y.shape[1])) * 2 - 1

def crossEntropy(y, ycap):
    y = np.array(y)
    ycap = np.array(ycap)
    left = y * np.log(ycap)
    rgt = (1-y) * np.log(1-ycap)
    lrsum = left + rgt
    s = lrsum.sum()
    ce = -s/len(y)
    return ce

ploss =0
flag =0
conv = 0.000001
for i in range(100000):
   ycap = prediction(X, W)
   e = Y - ycap
   closs = crossEntropy(Y, ycap)
   if i%1000 ==0 :
       print(f"current loss after {i+1} iterations {closs}")
   delta = e * derivative(ycap)
   W += X.T.dot(delta) * 0.02
   if  np.abs(ploss - closs ) <= conv:
      print(f"Training completed after {i+1} iterations ")
      flag = 1
      break
   ploss = closs
if flag==0:
   print("Training not Completed , run few more iterations ")

ycap=prediction(X,W)
ys=np.where(ycap>0.5,1,0) 

def accuracy(y,ycap):
   pnct=np.where(y==ycap)[0].size
   n = y.shape[0]
   return pnct/n * 100
acc=accuracy(Y,ys)
print(acc)

    

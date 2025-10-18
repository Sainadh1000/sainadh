age = [20, 25, 27, 22 , 24, 30, 35, 32, 40, 38]
experience = [0, 3, 5, 1, 2.5, 6, 10, 7, 11, 10.5]

#step1 array
import numpy as np
age=np.array(age)
experience=np.array(experience)
income = 3 + 2 * age + 1.5 * experience
ones=np.ones(len(age))
x=np.c_[ones,age,experience]
y=np.c_[income]

#step2 scaling
def scale(x):
   x = np.array(x)
   return (x - x.mean())/ x.std()
age_scale=scale(age)
experience_scale=scale(experience)
x_scale=np.c_[ones,age_scale,experience_scale]
y_scale=scale(y)
print(y_scale)

#step3 define weights
np.random.seed(101)
w= np.random.random((x_scale.shape[1], 1)) * 2 - 1

#step4 for loop for decreasing error
convergence=0.0000001
ploss=0
flag=0
for i in range(10000):
   ycap=x_scale.dot(w)
   closs = ((y_scale-ycap)**2).mean()
   if i%100==0:
      print("Current Loss ", closs)
   delta=x_scale.T.dot(y_scale-ycap) / ycap.shape[0]
   w +=delta*0.2
   if np.abs(ploss-closs) <= convergence:
       print(f" Training Completed after {i+1} iterations ")
       flag=1
       break
   ploss = closs
if flag==0:
   print("Training not completed , please run few more iterations ")
ycap = x_scale.dot(w)
np.c_[y_scale, ycap]
rss = ((y_scale-ycap)**2).sum()
tss = ((y_scale - y_scale.mean())**2).sum()
rsquare = 1- rss/tss
print("Accuracy ", rsquare*100)

y_prediction=y.std() * y_scale + y.mean()
print(y_prediction)
print(np.c_[y,y_prediction])


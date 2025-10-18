age =        [22, 24, 28, 30, 35, 40, 23, 26, 31, 37, 45, 29, 33, 21]
experience = [1,  2,  4,  6,  9, 12, 0.5, 3,  7, 10, 15, 5,  8,  0.2]
import numpy as np
age=np.array(age)
experience=np.array(experience)
income=3+0.5*age+2*experience
print(income)
ones=np.ones(len(age))
x=np.c_[ones,age,experience]
print(x)
y=np.c_[income]
print(y)

def scale(x):
    x=np.array(x)
    return (x-x.mean())/x.std()
age_scale=scale(age)
experience_scale=scale(experience)
x_scale=np.c_[ones,age_scale,experience_scale]
y_scale=scale(y)

np.random.seed(101)
w=np.random.random((x.shape[1],1))*2-1
print(w)

convergence=0.0000001
ploss=0
flag=0
for i in range(100000):
    ycap=x_scale.dot(w)
    closs=((y_scale-ycap)**2).mean()
    delta=x_scale.T.dot(y_scale-ycap)/y_scale.shape[0]
    if i%100==0:
        print("currentloss" ,closs)
    w +=delta*0.2
    if np.abs(ploss-closs) <=convergence:
        print(f"training complete after {i+1} iterations")
        flag=1
        break
if flag==0:
    print("training not complete run few more iterations")

ycap=x_scale.dot(w)
rss=((y_scale-ycap)**2).sum()
tss=((y_scale-y_scale.mean())**2).sum() 
accuracy=1-(rss/tss)*100
print(accuracy)

y_predictions=y.std()*y_scale + y.mean()
print(y_predictions)
print(np.c_[y,y_predictions])

rss_actual=((y-y_predictions)**2).sum()
tss_actual=((y-y.mean())**2).sum()
accuracy_actual=(1-(rss_actual/tss_actual))*100
print(accuracy_actual)


# step1:take inputs and outputs
# step2: create matrix for inputs and outputs
# step3: random weights
# step4: derivate
# step5: accuracy
import numpy as np
age = [21, 23, 26, 28, 31, 33, 36, 37, 39, 41]
experience = [0.5, 2, 3.5, 5, 6.5, 7.5, 9, 10, 11, 12]
age=np.array(age)
experience=np.array(experience)
income=3+0.3*age+2.5*experience
ones=np.ones(len(age))
x=np.c_[ones,age,experience]
y=np.c_[income]

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

convergence=0.000000001
ploss=0
flag=0
for i in range(10000):
    ycap=x_scale.dot(w)
    closs=((y_scale-ycap)**2).mean()
    delta=x_scale.T.dot(y_scale-ycap)/y_scale.shape[0]
    if i%100==0:
        print("current loss:",closs)
    w=delta*0.2
    if np.abs(ploss-closs)<=convergence:
        print(f"training completed after{i+1} iterations")
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

y_predictions=y.std()*y_scale + y.mean()
print(y_predictions)
print(np.c_[y,y_predictions])

rss_actual=((y-y_predictions)**2).sum()
tss_actual=((y-y.mean())**2).sum()
accuracy_actual=(1-(rss_actual/tss_actual))*100
print(accuracy_actual)








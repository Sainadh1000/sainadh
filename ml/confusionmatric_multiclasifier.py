import numpy as np
y = [0, 1,2,0,1,2,2,1,1,0,0,2,1,0]
ycap = [0,1,2,1,0,1,0,2,1,2,0,2,1,1]
l=len(set(y))
print(l)

def confusionmatrix(y,ycap):
    cm=np.zeros((l,l))
    for i,j in zip(y,ycap):
        cm[i,j]+=1
    return cm
cm=confusionmatrix(y,ycap)
print(cm)

def cmetrics(cm):
    p=[]
    r=[]
    r1=[]
    for i in range(cm.shape[0]):
        pc=round(float(cm[i,i]/cm[:,i].sum()),2)
        rc=round(float(cm[i,i]/cm[i].sum()),2)
        r1c=round(float(2*(pc*rc)/(pc+rc)),2)
        p.append(pc)
        r.append(rc)
        r1.append(r1c)
    return np.array((p, r, r1)).T
metrics=cmetrics(cm)   
print(metrics)
def accuracy(cm):
    return round(np.trace(cm)/cm.sum()*100,2)#trace(cm): sum of diagonal elements = correct predictions
acc=accuracy(cm)
print(f"accuracy:{acc}")
import numpy as np
y = [1,0,1,0,0,1,0,1,1,1,0,0]
ycap = [1,0,1,0,1,0,0,1,1,0,1,0]


def confusionmatrix(y,ycap):
    cm=np.zeros((2,2))
    for i,j in zip(y,ycap):
        cm[i,j]+=1
    return cm
cm=confusionmatrix(y,ycap)
print(cm)

TN=cm[0,0]
FN=cm[0,1]
FP=cm[1,0]
TP=cm[1,1]

precision=TP/cm[:,1].sum()
print(precision)

recall=TP/cm[1].sum()
print(recall)

r1score=2*(precision*recall)/(precision+recall)
print(r1score)

accuracy=(TP+TN)/cm.sum()
print(accuracy)

def cmetrics(cm):
    TN=cm[0,0]
    FN=cm[0,1]
    FP=cm[1,0]
    TP=cm[1,1]
    p=round(float(TP/cm[:,1].sum()),2)
    r=round(float(TP/cm[1].sum()),2)
    r1=round(float(2*(p*r)/(p+r)),2)
    acc=round(float((TP+TN)/cm.sum())*100,2)
    return (p,r,r1,acc)
metrics=cmetrics(cm)
print(metrics)



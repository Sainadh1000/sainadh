runs=[50,56,23,100,120,34,0,67,89,21,76,45]
average=sum(runs)/len(runs)
print(average)
classification=[]
for i in runs:
    if i>average:
        classification.append('above')
    else:
        classification.append('below')
abovecount=0
belowcount=0
for i in classification:
    if i=='above':
        abovecount+=1
    else:
        belowcount+=1
if abovecount>belowcount:
    print('most of runs are above average')
else:
    print('most of runs are below average')







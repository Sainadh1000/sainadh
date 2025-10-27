import numpy as np
temp=np.array([31, 33, 32, 34, 35, 33, 32, 31, 30, 29, 31, 32, 33, 34, 35, 36, 37, 36, 35, 34])
window=4
futurevalues=7
forecast=[]
for _ in range(futurevalues):
    if len(temp)<window:
        print("less no of data")
    next_value=np.mean(temp[-window])
    forecast.append(round(next_value,2))
    temp=np.append(temp,next_value)
for i,t in enumerate(forecast,start=21):
    print(f"the temparature of day{i}:{t}")
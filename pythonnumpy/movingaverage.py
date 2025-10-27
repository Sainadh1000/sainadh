import numpy as np
temp=np.array([30, 32, 31, 33, 34, 32, 31, 30, 29, 28,30, 31, 32, 33, 34, 35, 36, 35, 34, 33])
window=3
futurvalues=5
forecast=[]
data=temp.copy()
for _ in range(futurvalues):
    if len(data)<window:
        print("less no of data")
    
    next_data=np.mean(data[-window:])
    forecast.append(round(next_data,2))
    data=np.append(data,next_data)
for i, temparature in enumerate(forecast, start=21):
    print(f"Forecast Day {i}: {temparature} Degree-C")


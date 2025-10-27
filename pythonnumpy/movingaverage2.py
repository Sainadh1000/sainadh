import numpy as np
price = np.array([100, 120, 130, 145.5, 136, 127, 179, 180, 201.3, 220, 221, 200, 187.4, 183, 168, 160, 154, 151.6])
window=4
futurevalues=5
forecast=[]
data=price.copy()
for _ in range(futurevalues):
    if len(data)<window:
        raise ValueError("not enough no of data to calculate moving average")
    next_price=np.mean(data[-window:])
    forecast.append(round(next_price,3))
    data=np.append(data,next_price)
for i,predicted_price in enumerate(forecast,start=19):
    print(f"price of chicken in day{i} is {predicted_price}")
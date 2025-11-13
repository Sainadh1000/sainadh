import numpy as np 
import pandas as pd
df=pd.read_csv('ml/textfile.txt')
df.info()
x= df[['Age', 'BMI', 'Blood Pressure', 'Glucose Level', 'Insulin Level']]
y = df['diabetic_score']

#step1 split data 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=42
)

#step2 scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

#step3 neihbors
from sklearn.neighbors import KNeighborsRegressor
kreg = KNeighborsRegressor(n_neighbors=5)
kreg.fit(x_train_scaled, y_train)

#step4 r2score
from sklearn.metrics import r2_score
y_pred = kreg.predict(x_test_scaled)

print("R Score:", r2_score(y_test, y_pred))

newarray=np.array([[46, 27.2, 124, 142, 86]])
newarray_scaled=scaler.fit_transform(newarray)
predicted_score = kreg.predict(newarray_scaled)
print("Predicted Diabetic Score:", predicted_score[0])



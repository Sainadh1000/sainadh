import numpy as np
import pandas as pd

df=pd.read_csv('ml/textfile.txt')
df.info()
x = df[['Age', 'BMI', 'Blood Pressure', 'Glucose Level', 'Insulin Level']]
y=df['Diabetic Status'].map({'Yes':1,'No':0})
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
#the parameter stratify=y is used to make sure that the class distribution (proportion of labels) in your training and testing sets remains the same as in the original dataset.
    x,y,test_size=0.3,random_state=42,stratify=y
    )

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier(n_neighbors=5)
knc.fit(x_train_scaled, y_train)

from sklearn.metrics import accuracy_score
y_pred=knc.predict(x_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))

newdata=np.array([[46, 28.2, 120, 134, 81]])

newdata_scaler=scaler.fit_transform(newdata)

prediction = knc.predict(newdata_scaler)
print("Predicted Diabetic Status:", "Yes" if prediction[0] == 1 else "No")




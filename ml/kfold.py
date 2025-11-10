import pandas as pd 
import numpy as np
from sklearn.model_selection import KFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder,StandardScaler

df=pd.read_csv('ml/textfile.txt')
df=pd.DataFrame(df)

model=LogisticRegression()
Label_Encoder=LabelEncoder()

x = df[['Age', 'BMI', 'Blood Pressure', 'Glucose Level', 'Insulin Level']]
y=Label_Encoder.fit_transform(df['Diabetic Status'])
print(y)

scaler=StandardScaler()
x_scale=scaler.fit_transform(x)

kfold=KFold(n_splits=5,shuffle=True,random_state=42)
results=cross_val_score(model,x_scale,y,cv=kfold,scoring='accuracy')

print(f"accuracy scoress:{results}")
print(f"mean accuracy:{results.mean()*100}")

import pandas as pd
import numpy as np
from sklearn.model_selection import KFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder,StandardScaler

df = pd.read_csv('ml/multitextfile.txt', sep='\t')
df.info()
df=pd.DataFrame(df)

model=LogisticRegression()
Label_Encoder=LabelEncoder()
scaler=StandardScaler()

x = df[['Age', 'BMI', 'Blood Pressure', 'Glucose Level', 'Insulin Level']]
y=Label_Encoder.fit_transform(df['Diabetic Status'])
print(y)

x_scale=scaler.fit_transform(x)

kfold=KFold(n_splits=5,shuffle=True,random_state=42)
results=cross_val_score(model,x_scale,y,cv=kfold,scoring='accuracy')

print(f"accuracy scores:{results}")
print(f"mean of accuracy scores:{results.mean()*100}")

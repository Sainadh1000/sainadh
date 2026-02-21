data={'id': [101, 102, 103, 104, 105],
 'name': ['Ravi', 'Giri', 'Siri', 'Venu', 'Veni'],
 'salary': [10000, 20000, 90000, 100000, 70000],
 'gender': ['m', 'm', 'f', 'm', 'f'],
 'dno': [11, 12, 13, 11, 12],
 'last_name':['smith','devon','tennyson','danvers','carson']}

import pandas as pd
df=pd.DataFrame(data)
print(df)

print(df['name'])

df['fullname']=df['name'] + df['last_name']
print(df['fullname'])

print(df.describe())
print(df.info())
print(df.isna())

print(df.head())

#  id  name  salary gender  dno last_name      fullname
# 0  101  Ravi   10000      m   11     smith     Ravismith
# 1  102  Giri   20000      m   12     devon     Giridevon
# 2  103  Siri   90000      f   13  tennyson  Siritennyson
# 3  104  Venu  100000      m   11   danvers   Venudanvers
# 4  105  Veni   70000      f   12    carson    Venicarson

print(df.head(3))

#     id  name  salary gender  dno last_name      fullname
# 0  101  Ravi   10000      m   11     smith     Ravismith
# 1  102  Giri   20000      m   12     devon     Giridevon
# 2  103  Siri   90000      f   13  tennyson  Siritennyson

print(df.tail())

#  id  name  salary gender  dno last_name      fullname
# 0  101  Ravi   10000      m   11     smith     Ravismith
# 1  102  Giri   20000      m   12     devon     Giridevon
# 2  103  Siri   90000      f   13  tennyson  Siritennyson
# 3  104  Venu  100000      m   11   danvers   Venudanvers
# 4  105  Veni   70000      f   12    carson    Venicarson

print(df.tail(2))
#  id  name  salary gender  dno last_name     fullname
# 3  104  Venu  100000      m   11   danvers  Venudanvers
# 4  105  Veni   70000      f   12    carson   Venicarson

newdf = df[['id', 'salary', 'gender']]
print(newdf)

print(df.iloc[2])
# id                    103
# name                 Siri
# salary              90000
# gender                  f
# dno                    13
# last_name        tennyson
# fullname     Siritennyson
# Name: 2, dtype: object

print(df.iloc[-2])


# id                   104
# name                Venu
# salary            100000
# gender                 m
# dno                   11
# last_name        danvers
# fullname     Venudanvers
# Name: 3, dtype: object

print(df.iloc[~1])
print(df.iloc[2:, 1:-1])

print(df[df['salary']==90000])

print(df[(df['salary']>90000) & (df['dno']==11)])

df['salary'] += df['salary'] * 0.1

df['tax']  = df['salary'] * 0.1
df['hra'] = df['salary'] * 0.2
df['netsal'] =   df['salary'] + df['hra'] - df['tax']

totalsum= df['salary'].sum()
print(totalsum)


newdata = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 15, 30, 10, 25]
}

xdf = pd.DataFrame(newdata)
print(xdf)

xdf.groupby('Category').sum()
print(xdf.groupby('Category').sum())
print(xdf.groupby('Category').max())
print(xdf.groupby('Category').count())

grouped = xdf.groupby('Category').agg({
    'Values': ['sum', 'mean', 'max', 'min']
})

print(grouped)

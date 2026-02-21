import pandas as pd
df=pd.read_csv('./pandas/file.txt')
cols=['id','name','salary','gender','dno']
df=pd.read_csv('./pandas/file.txt',header=None,names=cols)
print(df)


df['gender']=df['gender'].replace({'m':'male','f':'female'})
print(df)

dept = {11 : 'Marketing', 12: 'Hr', 13: 'Finance'}
df['dname'] = df['dno'].map(dept).fillna('Other')
print(df)

def toGender(g):
   gend = 'Invalid'
   if g=='male':
      gend = 'm'
   elif g=='female':
      gend = 'f'
   return gend


def toGrade(sal):
   grade = 'D'
   if sal>=100000:
     grade = 'A'
   elif sal>=75000:
     grade = 'B'
   elif sal>=50000:
     grade = 'C'
   return grade

df['gender']=df['gender'].apply(toGender)
print(df['gender'])

df['grade']=df['salary'].apply(toGrade)
print(df['grade'])

df.to_csv('./pandas/empnew.txt')
df.to_csv('./pandas/emptransformed.txt', index = False)
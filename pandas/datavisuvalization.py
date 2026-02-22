import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('./pandas/emptransformed.txt')
print(df)

#heatmap
corr=df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True,cmap="coolwarm",fmt=".2f")
plt.show()


sns.histplot(df['salary'],kde=True)
plt.show()
sns.boxenplot(x=df['salary'])
plt.show()
sns.violinplot(x=df['salary'])
plt.show()


sns.scatterplot(x="dno", y="salary", data=df)
plt.show()

sns.pairplot(df)
plt.show()

sns.lineplot(x="dno", y="salary", data=df)
plt.show()



sns.countplot(x=df['gender'])
plt.show()

sns.barplot(x="dno", y="salary", data=df)
plt.show()

sns.heatmap(df.isnull(), cbar=False)
plt.show()

sns.kdeplot(df["salary"])
plt.show()

sns.jointplot(x="dno", y="salary", data=df, kind="scatter")

plt.show()
sns.clustermap(df.corr(numeric_only=True))
plt.show()
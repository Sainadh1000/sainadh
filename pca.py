from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Math": [90, 85, 88, 92, 95, 70, 60, 75, 85, 95],
    "Physics": [91, 86, 89, 93, 96, 72, 65, 78, 88, 97],
    "Chemistry": [88, 82, 85, 90, 94, 68, 62, 74, 84, 93]
}

df=pd.DataFrame(data)

scaler=StandardScaler()
df=scaler.fit_transform(df)
pca=PCA(n_components=2)
principal_components = pca.fit_transform(df)
pca_df=pd.DataFrame(data=principal_components,columns=["PC1","PC2"])

print("\nExplained Variance Ratio:", pca.explained_variance_ratio_)
plt.figure()
plt.scatter(pca_df["PC1"], pca_df["PC2"])
plt.xlabel("priciple component1")
plt.ylabel("principle label2")
plt.title("Principle component anaysis")
plt.show()
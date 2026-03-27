from sklearn.cluster import KMeans
import numpy as np

a=[1,2,3,4,5,6,7,8,9,10]
b=[20,34,56,78,90,120,150,200,234,267]
c=[5,8,12,15,23,28,34,39,43,49]

x=np.c_[a,b,c]

km=KMeans(n_clusters=3,random_state=0).fit(x)
print("labels :",km.labels_)
print("centers :",km.cluster_centers_)
n=[[11,287,56]]
c=km.predict(n)
print("class of n:",c)


from scipy.cluster.hierarchy import dendrogram,fcluster,linkage
import matplotlib.pyplot as plt

z=linkage(x,'ward')
dendrogram(z)
plt.show()
clusters = fcluster(z,t=4,criterion='maxclust')
print(clusters)


from sklearn.cluster import DBSCAN

db=DBSCAN(eps=0.8,min_samples=3).fit(x)
print("labelsL",db.labels_)



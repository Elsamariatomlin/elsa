import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# customer=['CustomerID,Gender,Age,Annual Income (k$),Spending Score (1-100)']
df=pd.read_csv("C:\\Users\\pc26\\Desktop\\elsamca\\customer.csv")

print("customer data")
print(df.isnull().sum())

X=df.iloc[:,[3,4]].values
print(X)

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

#elbow graph
sns.set()
plt.plot(range(1,11),wcss)
plt.title("elbow graph")
plt.xlabel("number of clusters")
plt.ylabel("wcss")
plt.show()
 #optimum number of clusters=5
KMeans=KMeans(n_clusters=5,init='k-means++',random_state=42)
Y = kmeans.fit_predict(X)
print(Y)

clusters=0,1,2,3,4
plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0],X[Y==0,1],s=50, c='blue',label='cluster 1')
plt.scatter(X[Y==1,0],X[Y==1,1],s=50, c='red',label='cluster 2')
plt.scatter(X[Y==2,0],X[Y==2,1],s=50, c='green',label='cluster 3')
plt.scatter(X[Y==3,0],X[Y==3,1],s=50, c='yellow',label='cluster 4')
plt.scatter(X[Y==4,0],X[Y==4,1],s=50, c='violet',label='cluster 5')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='cyan',label='centroids')

plt.title("customer groups")
plt.xlabel("annual income")
plt.ylabel("spending score")
plt.legend()
plt.show()
#step to remember in scatter
#1.choose number of clusters
#2.choose random k points
#3.assign each data point to the closest centroid
#4.recompute centroids of each cluster
#5.repeat steps 3 and 4 until convergence



#from start to end
#1.preprocess data
#2.load algorithm
#3.predict elbow  graph
#4.cluster of elbow graph data to algorithm
#5.visualize clusters
#6.plot graphj
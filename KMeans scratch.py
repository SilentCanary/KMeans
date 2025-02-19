
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class KMeansClustering():
    
    def __init__(self,X,num_clusters):
        self.K=num_clusters
        self.max_iterations=1000
        self.num_examples,self.num_features=X.shape
        pass
    
    
    
    def initialize_random_centroids(self,X):
        centroids=np.zeros((self.K,self.num_features))
        for k in range(self.K):
            centroid=X[np.random.choice(range(self.num_examples))]
            centroids[k]=centroid
        return centroids
    
       
    
    def create_clusters(self,X,centroids):
        clusters=[[] for _ in range(self.K)]
        for point_idx,point in enumerate(X):
            closest_centroid=np.argmin(np.sqrt(np.sum((point-centroids)**2,axis=1)))
            clusters[closest_centroid].append(point_idx)
            
        return clusters
    
    def calculate_new_centroids(self,clusters,X):
        centroids=np.zeros((self.K,self.num_features))
        for idx,cluster in enumerate(clusters):
            new_centroid=np.mean(X[cluster],axis=0)
            centroids[idx]=new_centroid
            
        return centroids
    
    def predict_cluster(self,clusters,X):
        
        y_pred=np.zeros(self.num_examples)
        for cluster_idx,cluster in enumerate(clusters):
            for sample_idx in cluster:
                y_pred[sample_idx]=cluster_idx
        return y_pred
    
    def plot_figures(self,X,y):
        plt.scatter(X[:,0],X[:,1] ,c=y,s=40,cmap=plt.cm.Spectral )
        plt.show()
    
    def fit(self,X):
        centroids=self.initialize_random_centroids(X)
        for it in range(self.max_iterations):
            clusters=self.create_clusters(X, centroids) 
            previous_centroids=centroids
            centroids=self.calculate_new_centroids(clusters, X) 
            diff=centroids-previous_centroids
            if not diff.any():
                print("terminated")
                break
        y_pred=self.predict_cluster(clusters, X)
        if self.plot_figures:
            self.plot_figures(X, y_pred)
        return y_pred
    
if __name__=='__main__':
    np.random.seed(10)
    num_clusters=3
    X,_ =make_blobs(n_samples=1000,n_features=2,centers=num_clusters)
    KMeans=KMeansClustering(X, num_clusters)
    y_pred=KMeans.fit(X)
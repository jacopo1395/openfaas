import numpy as np
from sklearn.cluster import KMeans
import json

# def handle(req):
#     v = req.split("|");
#     data = []
#     for elem in v:
#         current_array = elem.split(",");
#         numeric_array = [float(numeric_string) for numeric_string in current_array]
#         data.append(numeric_array)
#     X = np.array(data)
#     # Number of clusters
#     kmeans = KMeans(n_clusters=len(data))
#     # Fitting the input data
#     kmeans = kmeans.fit(X)
#     # Getting the cluster labels
#     labels = kmeans.predict(X)
#     # Centroid values
#     # centroids = kmeans.cluster_centers_
#     # Comparing with scikit-learn centroids
#     # print(C) # From Scratch
#     # print(centroids) # From sci-kit learn
#     print(labels)
#     # print(centroids)

def handle(req):
    j = json.loads(req)
    data = j["dataset"]
    l = j["n_clusters"]
    X = np.array(data)
    kmeans = KMeans(n_clusters=l)
    kmeans = kmeans.fit(X)
    labels = kmeans.predict(X)
    centroids = kmeans.cluster_centers_
    print(centroids) # From sci-kit learn
    print(labels)

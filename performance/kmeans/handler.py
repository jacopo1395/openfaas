import numpy as np
from sklearn.cluster import KMeans
import json

def handle(req):
    j = json.loads(req)
    dataset = j["dataset"]
    data = []
    for value in dataset:
        data.append(value["vector"])
    l = j["n_clusters"]
    # print(data)
    X = np.array(data)
    kmeans = KMeans(n_clusters=l)
    kmeans = kmeans.fit(X)
    labels = kmeans.predict(X)
    centroids = kmeans.cluster_centers_
    print(centroids) # From sci-kit learn
    print(labels)

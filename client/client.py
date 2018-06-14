import sys
import time
import json
import random
import openfaas
import rabbitmq


# Data ################
j = {"data":[]}
data = rabbitmq.dataset_temp();
j["data"] = data
array = json.dumps(j)

j={
    "X_train":[

            {"vector":[1]},
            {"vector":[2]},
            {"vector":[3]}

    ],
    "X_test":[

            {"vector":[1]},
            {"vector":[2]},
            {"vector":[3]}

    ],
    "y_train":[1,2,3],
    "y_test":[1,2,3]
}

json_data1 = json.dumps(j)

j = {
    "dataset":[

            {"vector":[1,2]},
            {"vector":[5,8]},
            {"vector":[8,8]},
            {"vector":[1,0.6]},
            {"vector":[9,11]}
    ],
    "n_clusters": 2
}

json_data2 = json.dumps(j)
#########################


lvl = int(sys.argv[1])

if lvl==1:
    openfaas.mean(array)
if lvl==2:
    openfaas.peakdetection(array)
if lvl==3:
    openfaas.kmeans(json_data2)

import time
import json
import threading
import random

import openfaas
import rabbitmq
import matplotlib.pyplot as plt


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
# print(array)

def rand_color(n):
    return (random.uniform(0.0, 1.0),random.uniform(0.0, 1.0),random.uniform(0.0, 1.0) )

def consumer(cond, lvl):
    with cond:
        cond.wait()
        if lvl==1:
            openfaas.mean(array)
        if lvl==2:
            openfaas.peakdetection(array)
        if lvl==3:
            openfaas.kmeans(json_data2)


print("Start with different number of threads and Difficulty")
print("1=mean/min/max - 2=peak detection - 3=kmeans/regression")
n=11
for lvl in range(1,4):
    print(lvl)
    latency = []
    for i in range (1,n):
        # print(i)
        condition = threading.Condition()
        threads = []
        for j in range(0,i*1): # start all threads
            t = threading.Thread(name='t', target=consumer, args=(condition,lvl))
            threads.append(t)
            t.start()
        # print("start")
        before = int(round(time.time() * 1000)) # start time

        with condition:
            condition.notifyAll()
        for t in threads:
            t.join()

        after = int(round(time.time() * 1000)) # stop time
        delta = after-before
        # print("stop")

        # print("")
        print("Threads: " + str(len(threads)))
        # print("Difficulty: " + str(lvl))
        # print("Milliseconds: " + str(delta))
        # print("Latency: " + str(delta/len(threads)))
        latency.append(delta/len(threads))
    plt.plot(range(1,n), latency, color=rand_color(i), label="Difficulty "+str(lvl))
plt.ylabel('Milliseconds')
plt.xlabel('Threads')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


def collect_data():
    # TODO
    print("todo")


# openfaas.test(openfaas.mean, array)
# openfaas.test(openfaas.minimun, array)
# openfaas.test(openfaas.maximum, array)
# openfaas.test(openfaas.peakdetection, array)
# openfaas.test(openfaas.regression, json_data1)
# openfaas.test(openfaas.kmeans, json_data2)

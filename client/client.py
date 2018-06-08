import time
import json
import threading
import random

import openfaas
import rabbitmq
import matplotlib.pyplot as plt
import sys

# print(sys.argv)


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

if (len(sys.argv)<4):
    print("How to use:")
    print("\tpython3 client.py <max_threads> <step_range> <max_difficulty> ")
    sys.exit("\nERROR: few parameters")

print("Start with different number of threads and Difficulty")
print("1=mean/min/max - 2=peak detection - 3=kmeans/regression")
n = int(sys.argv[1]) + 2
step = int(sys.argv[2])
d = int(sys.argv[3]) + 1
for lvl in range(1,d):
    latency = []
    for i in range (1,n,step):
        condition = threading.Condition()
        threads = []
        # start all threads
        for j in range(0,i):
            t = threading.Thread(name='t', target=consumer, args=(condition,lvl))
            threads.append(t)
            t.start()

        # start time
        before = int(round(time.time() * 1000))
        with condition:
            condition.notifyAll()
        for t in threads:
            t.join()
        # stop time
        after = int(round(time.time() * 1000))
        delta = after-before

        print("")
        print("Threads: " + str(len(threads)))
        print("Difficulty: " + str(lvl))
        print("Milliseconds: " + str(delta))
        print("Latency: " + str(delta/len(threads)))
        latency.append(delta/len(threads))
    plt.plot(range (1,n,step), latency, color=rand_color(i), label="Difficulty "+str(lvl))
plt.ylabel('Milliseconds')
plt.xlabel('Threads')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()



# openfaas.test(openfaas.mean, array)
# openfaas.test(openfaas.minimun, array)
# openfaas.test(openfaas.maximum, array)
# openfaas.test(openfaas.peakdetection, array)
# openfaas.test(openfaas.regression, json_data1)
# openfaas.test(openfaas.kmeans, json_data2)

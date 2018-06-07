import requests
import time
import json


def collect_data():
    # TODO
    print("todo")



def test(function, data):
    before = int(round(time.time() * 1000))
    function(data)
    after = int(round(time.time() * 1000))
    delta = after-before
    print("")
    print("Function: "+function.__name__ )
    print("Time in milliseconds: " + str(delta))
    print("")


def mean(array):
    r = requests.post('http://127.0.0.1:8080/function/mean', data=array)
    # print(r)

def minimun(array):
    r = requests.post('http://127.0.0.1:8080/function/min', data=array)
    # print(r)

def maximum(array):
    r = requests.post('http://127.0.0.1:8080/function/max', data=array)
    # print(r)

def kmeans(json_obj):
    r = requests.post('http://127.0.0.1:8080/function/kmeans', data=json_obj)
    # print(r)

def peakdetection(json_obj):
    r = requests.post('http://127.0.0.1:8080/function/peakdetection', data=json_obj)
    # print(r)


j = {"data":[1,2,3]}
array = json.dumps(j)

test(mean, array)
test(minimun, array)
test(maximum, array)
test(peakdetection, array)


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

json_data = json.dumps(j)
test(kmeans, json_data)

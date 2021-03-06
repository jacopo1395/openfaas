import requests

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
    r = requests.post('http://127.0.0.1:8080/function/kmeansjs', data=json_obj)
    # print(r)

def peakdetection(json_obj):
    r = requests.post('http://127.0.0.1:8080/function/peakdetectionjs', data=json_obj)
    # print(r)

def regression(json_obj):
    r = requests.post('http://127.0.0.1:8080/function/regressionjs', data=json_obj)
    # print(r)


def test(function, data):
    before = int(round(time.time() * 1000))
    function(data)
    after = int(round(time.time() * 1000))
    delta = after-before
    print("")
    print("Function: "+function.__name__ )
    print("Time in milliseconds: " + str(delta))
    print("")

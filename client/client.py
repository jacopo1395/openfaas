import requests
import time
import numpy as np


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


def call_mean(array):
    r = requests.post('http://127.0.0.1:8080/function/mean', data=array)
    print(r)

def call_min():
    r = requests.post('http://127.0.0.1:8080/function/min', data=array)
    print(r)

def call_max():
    r = requests.post('http://127.0.0.1:8080/function/max', data=array)
    print(r)


array = "5,21.5,-9"

test(call_mean, array)
test(call_min, array)
test(call_max, array)

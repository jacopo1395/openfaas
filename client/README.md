# Client
This is a project to perform a benchmark on openfaas.

The client.py spawns a different number of threads (you choose how many) and executes one of the three types of functions (you choose which one) with different computational costs: *Easy*, *Medium* and *Hard*.
All the threads perform the **same function** and start at the **same time**.

# Functions

These are the functions written in python but there is a copy of them in the node to run on a Raspberry pi.

Each function is accessible via a **POST request** with parameter a **JSON object**.

## Easy

**mean**
``` json
{"data":[1,2,3,...]}
```
**min**
``` json
{"data":[1,2,3,...]}
```
**max**
``` json
{"data":[1,2,3,...]}
```

## Medium

**peakdetection**
``` json
{"data":[1,2,3,...]}
```

## Hard

**kmeans**
``` json
{
    "dataset":[

            {"vector":[1,2,...]},
            {"vector":[1,2,...]},
            {"vector":[1,2,...]},
            ...

    ],
    "n_clusters": 2
}
```
>len(dataset) >= n_clusters



**regression**
``` json
{
    "X_train":[

            {"vector":[1,...]},
            {"vector":[1,...]},
            {"vector":[1,...]},
            ...

    ],
    "X_test":[

            {"vector":[1,...]},
            {"vector":[1,...]},
            {"vector":[1,...]},
            ...

    ],
    "y_train":[1,2,3,...],
    "y_test":[1,2,3,...]
}
```
>len(X_train) = len(y_train)

>len(X_test) = len(y_test)


# Datasets

To test the functions I used a real time datasets. You can find it in the datasets folder in this repository.
In the directory there are some text file and in each file there are data coming from a type of sensor.

You can update manually the datasets at any time by running `python3 rabbitmq.py`.

Each file is in CSV format (Comma-separated values):
> id_sensor,timestamp,value

To perform the benchmark a thread use this dataset and sends it in JSON format with a POST request to openfaas.



# How to Run
## Dependencies
First install all the dependencies:

`sudo pip3 install python-tk`

`sudo apt-get install python-matplotlibk`


# Run
command:

`python3 client.py <max_threads> <step_range> <max_difficulty>`


- **max_threads**: the maximum number of Threads. client.py tries the same function with different number of threads (range from 1 to max_threads).

- **step_range**: you can choose a step of the range from 1 to max_threads, the step is equals to step_range.

- **max_difficulty**: client.py executes the functions from easy level up to max_difficulty (easy=1, medium=2, hard=3).

*Example*: `python3 client.py 7 3 2` call the easy function with 1 thread then with 4 and finally with 7 threads; call the medium function with 1 then 4 and finally 7 threads.

```python
for i in range(1, max_threads, step_range):
        for j in range(1, max_difficulty):
            # call to openfaas function
```


# Results
For the tests I used 3 types of machines: an i7 4790, i7 3610QM and a Raspberry Pi model B.

## Latency

The latency is the equals to time/n_threads.
For each processor there is a latency based on the type of function.

| Processor | Easy | Medium | Hard |
|-|:-:|:-:|:-:|
| i7 4790 |-|-|-|
| i7 3610QM | 65.28 | 275.43 | 576.0|
| Pi |-|-|-|


## Chart

Test on i7 3610QM, from 1 to 11 threads, all the types of functions:
![alt text](https://raw.githubusercontent.com/jacopo1395/openfaas/master/client/Easy-Medium-Hard_10Threads.png)


Test on i7 3610QM, from 1 to 100 threads, only easy functions:
![alt text](https://raw.githubusercontent.com/jacopo1395/openfaas/master/client/Easy_1000Threads.png)


Other tests coming soon.

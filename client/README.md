# Client
This is a project to perform a benchmark on openfaas.

The start.c spawns a different number of threads (you choose how many) and executes one of the three types of functions (you choose which one) with different computational costs: *Easy*, *Medium* and *Hard*.
All the threads perform the call of the **same function** to openfaas and start at the **same time**.

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

To test the functions I used a real time datasets. You can find it in the [datasets folder](https://github.com/jacopo1395/openfaas/tree/master/client/datasets).
In the directory there are some text file and in each file there are data coming from a type of sensor.

You can update manually the datasets at any time by running `python dataset.py`.

Each file is in CSV format (Comma-separated values):
> id_sensor,timestamp,value

To perform the benchmark a thread use this dataset and sends it in JSON format with a POST request to openfaas.

## Example

This is a snippet of dataset file with the values of a temperature sensor

```
0013a20040c24039/0x312/temp,1528986126981,29.89
0013a200409c168b/0x383/temp,1528986127363,34.79
0013a20040a1d47f/0xa97/temp,1528986127402,26.0
0013a20040a1d88c/0x694/temp,1528986127941,35.13
```

# How to Run
## Compilation

`gcc ./start.c -lpthread`

# Run
command:

`./a.out <max_threads> <step_range> <max_difficulty>`


- **max_threads**: the maximum number of Threads. start.c tries the same function with different number of threads (range from 1 to max_threads).

- **step_range**: you can choose a step of the range from 1 to max_threads, the step is equals to step_range.

- **max_difficulty**: start.c executes the functions from easy level up to max_difficulty (easy=1, medium=2, hard=3).


*Example*: `./a.out 10 5 2` call the easy function with 1 thread then with 5 and finally with 10 threads; call the medium function with 1 then 5 and finally 10 threads.

Logic in C code:
```C
for (int i=1; i<=max_difficulty; i++){
    for (int j=0; j<=max_threads; j+=step_range){
        // if j=0 is considered equals 1
        // call to openfaas function
    }
}
```


# Results
For the tests I used 3 types of machines: an i7 4790, i7 3610QM and a Raspberry Pi model B.

## Latency

The latency is the equals to time/n_threads.
For each processor there is a latency based on the type of function.


<table class="tg">
  <tr>
    <th class="tg-p8bj">Processor</th>
    <th class="tg-7btt">Threads</th>
    <th class="tg-7btt">Easy</th>
    <th class="tg-7btt">Medium</th>
    <th class="tg-7btt">Hard</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3">Raspberry Pi</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">0.005000</td>
    <td class="tg-c3ow">0.002000</td>
    <td class="tg-c3ow">0.003000</td>
  </tr>
  <tr>
    <td class="tg-c3ow">10</td>
    <td class="tg-c3ow">0.723200</td>
    <td class="tg-c3ow">0.688400</td>
    <td class="tg-c3ow">0.726100</td>
  </tr>
  <tr>
    <td class="tg-c3ow">100</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">-</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3">i7 3610QM</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">0.002000</td>
    <td class="tg-c3ow">0.001000</td>
    <td class="tg-c3ow">0.001000</td>
  </tr>
  <tr>
    <td class="tg-c3ow">10</td>
    <td class="tg-c3ow">0.245200</td>
    <td class="tg-c3ow">0.200000</td>
    <td class="tg-c3ow">0.245800</td>
  </tr>
  <tr>
    <td class="tg-c3ow">100</td>
    <td class="tg-c3ow">0.747060</td>
    <td class="tg-c3ow">0.598670</td>
    <td class="tg-c3ow">0.736790</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3">i7 4790</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">0.001000</td>
    <td class="tg-c3ow">0.000000</td>
    <td class="tg-c3ow">0.000000</td>
  </tr>
  <tr>
    <td class="tg-c3ow">10</td>
    <td class="tg-c3ow">0.302000</td>
    <td class="tg-c3ow">0.170700</td>
    <td class="tg-c3ow">0.175100</td>
  </tr>
  <tr>
    <td class="tg-c3ow">100</td>
    <td class="tg-c3ow">0.428780</td>
    <td class="tg-c3ow">0.415490</td>
    <td class="tg-c3ow">0.503520</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3">Swarm (2 devices)</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">0.001000</td>
    <td class="tg-c3ow">0.001000</td>
    <td class="tg-c3ow">0.000000</td>
  </tr>
  <tr>
    <td class="tg-c3ow">10</td>
    <td class="tg-c3ow">0.333800</td>
    <td class="tg-c3ow">0.166200</td>
    <td class="tg-c3ow">0.161700</td>
  </tr>
  <tr>
    <td class="tg-c3ow">100</td>
    <td class="tg-c3ow">0.458110</td>
    <td class="tg-c3ow">0.440300</td>
    <td class="tg-c3ow">0.423090</td>
  </tr>
</table>

To see detailed results open "result_*.txt" files in this repository.

## Chart
You can generate a chart with the result.txt file using:

`python3 chart.py`

----

Test on i7 3610QM, from 1 to 100 threads, all the types of functions:
![alt text](https://raw.githubusercontent.com/jacopo1395/openfaas/master/client/Figure_i7-3610QM.png)


Test on Raspberry Pi, from 1 to 10 threads, all the types of functions:
![alt text](https://raw.githubusercontent.com/jacopo1395/openfaas/master/client/Figure_pi.png)

Test on Docker Swarm with two i7 processors, from 1 to 100 threads, all the types of functions:
![alt text](https://raw.githubusercontent.com/jacopo1395/openfaas/master/client/Figure_swarm.png)

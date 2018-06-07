# Functions

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
len(dataset) >= n_clusters


## Hard

**kmeans**
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
len(X_train) = len(y_train)


len(X_test) = len(y_test)

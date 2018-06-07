import numpy as np
import peakutils

def handle(req):
    current_array = req.split(",");
    data = [float(numeric_string) for numeric_string in current_array]
    cb = np.array(data)
    indexes = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=100)
    print(indexes)

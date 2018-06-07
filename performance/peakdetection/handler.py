import numpy as np
import peakutils
import json

def handle(req):
    # current_array = req.split(",");
    # data = [float(numeric_string) for numeric_string in current_array]
    j = json.loads(req)
    data = j["data"]
    cb = np.array(data)
    indexes = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=100)
    print(indexes)

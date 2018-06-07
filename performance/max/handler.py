import json

def handle(req):
    # current_array = req.split(",");
    # data = [float(numeric_string) for numeric_string in current_array]
    j = json.loads(req)
    data = j["data"]
    m = max(data)
    print (m)

def handle(req):
    current_array = req.split(",");
    data = [float(numeric_string) for numeric_string in current_array]
    m = min(data)
    print (m)

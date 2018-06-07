def handle(req):
    current_array = req.split(",");
    data = [float(numeric_string) for numeric_string in current_array]
    m = mean(data)
    print (m)


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

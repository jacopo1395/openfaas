import requests
import json
import os

def download(n):
    url = "http://broker.sparkworks.net/api/queues/%2F/ichatz-annotated-readings/get"

    payload = {"count":n,"requeue":True,"encoding":"auto","truncate":50000}
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic aWNoYXR6OmoycGV3cWNLNGtIOUFhRFFrb3p4",
        'Cache-Control': "no-cache",
        'Postman-Token': "8e622988-c9f1-46df-a029-7ede246938fa"
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    # print response.text
    res = json.loads(response.text)
    # print "ciao"
    first = res[0]["payload"].split(",")[2]
    last = res[len(res)-1]["payload"].split(",")[2]
    print (int(last)-int(first))

    for name in os.listdir("./datasets"):
        # print name
        f1=open("./datasets/"+name, 'w')
        f1.write("")
        f1.close()


    for i in range(0,len(res)):
        data = res[i]["payload"].split(",")
        sensor = data[0]
        value = data[1]
        timestamp = data[2]
        s = sensor.split("/")
        if len(s)>2:
            s.pop(0)
        s.pop(0)
        sensorname = "_".join(s)
        name = "./datasets/dataset_"+sensorname+".txt"
        f1=open(name, 'a+')
        f1.write(sensor + "," + timestamp + "," + value+"\n")
        f1.close()
        # print timestamp



def dataset(name):
    lines = [line.rstrip('\n') for line in open(name)]
    values = []
    for line in lines:
        v = line.split(",")[2]
        values.append(v)
    return values

def dataset_temp():
    return dataset("./datasets/dataset_temp.txt");
def dataset_light():
    return dataset("./datasets/dataset_light.txt");
def dataset_sound():
    return dataset("./datasets/dataset_sound.txt");
def dataset_humid():
    return dataset("./datasets/dataset_humid.txt");

# curl 'http://broker.sparkworks.net/api/queues/%2F/ichatz-annotated-readings/get'
# -H 'authorization: Basic aWNoYXR6OmoycGV3cWNLNGtIOUFhRFFrb3p4'
# -H 'Origin: http://broker.sparkworks.net'
#  -H 'Accept-Encoding: gzip, deflate'
#  -H 'Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7'
#  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
#  -H 'Content-Type: text/plain;charset=UTF-8'
#   -H 'Accept: */*'
#   -H 'x-vhost: /'
#   -H 'Referer: http://broker.sparkworks.net/'
#   -H 'Cookie: m=2258:aWNoYXR6OmoycGV3cWNLNGtIOUFhRFFrb3p4'
#   -H 'Connection: keep-alive'
#   --data-binary '{"vhost":"/","name":"ichatz-annotated-readings","truncate":"50000","requeue":"true","encoding":"auto","count":"1"}'
#    --compressed

import snowboydecoder
import sys
import signal
import requests
import os
import subprocess


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def weather():
    r = requests.post('http://127.0.0.1:8080/function/weather', data='roma')
    # print(r.json())
    res = r.json()['weather'][0]['description']
    # print(res)
    temp = str(r.json()['main']['temp'])
    res = 'in Rome now there is '+res+' and the temperature is '+temp+' degrees celsius'
    cmd = 'say '+res
    print("")
    print (res)
    print("")
    # subprocess.check_output(['say', res])
    os.system(cmd)

def telegram():
    r = requests.post('http://127.0.0.1:8080/function/telegram', data='Hi everyone!')
    print ('ok, I did')
    os.system('say "ok, I did"')

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]


# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

w = weather
t = telegram

# sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=w,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)


detector.terminate()

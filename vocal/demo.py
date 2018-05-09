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
    print (res)
    # subprocess.check_output(['say', res])
    os.system(cmd)

def telegram():
    r = requests.post('http://127.0.0.1:8080/function/telegram', data='Hi everyone!')
    print ('ok, I send you a message')
    os.system('say "ok, I send you a message"')

if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

w = weather
t = telegram

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')


# main loop
detector.start(detected_callback=[w,t],
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

from datetime import datetime
import json
import random
import struct
import os
import signal
import requests
import sys
import RPi.GPIO as GPIO 
import time
import sys
import Adafruit_DHT as dht
# from local_database import * #from server_protocol import * from datetime import datetime

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)  # set GPIO Pins 


#DHT11
GPIO_DATA=4


# set GPIO direction (IN / OUT) 
GPIO.setup(GPIO_DATA, GPIO.IN) 



server_domain = 'http://45.77.39.49:8080/api/v1/'
token = 'dqm49B2LPqJUxEvpkCqT'
url_api_data = '/attributes'


def send_data_to_server():
    global response
    print('sending data...')
    humidity,temperature = dht.read_retry(dht.DHT11, 4)
    humidity = round(humidity, 2)
    temperature = round(temperature, 2)

    url = server_domain + token + url_api_data
    headers = {'content-type': 'application/json'}
    payload = {
        "temperature"	: temperature, 
        "humidity"	: humidity,
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.status_code)
    return response

while True:
    try:
        send_data_to_server()
    except KeyboardInterrupt:
        # ser thread.stop()
        sys.exit()

    else:
        if (response.status_code == 200):
            print("posting data OK")

        if (response.status_code == 201):
            print(response.status_code)
            print("posting data OK")
            print("")
    time.sleep(3)

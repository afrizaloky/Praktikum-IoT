import os import time import sys
import Adafruit_DHT as dht import paho.mqtt.client as mqtt import json

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT11.

try:
    while True:
        humidity, temperature = dht.read_retry(dht.DHT11, 4)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print(u"Temperature: {: g}\u00b0C, Humidity:{: g} %".format(
            temperature, humidity))

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

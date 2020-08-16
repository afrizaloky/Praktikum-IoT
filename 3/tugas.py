
# Libraries gnd  echo trig vcc
import paho.mqtt.client as mqtt 
import json
import RPi.GPIO as GPIO 
import time
import sys
import os
import Adafruit_DHT as dht

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)  # set GPIO Pins 

# HCSR04
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO_DATA=4


# set GPIO direction (IN / OUT) 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT) 
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_DATA, GPIO.IN) 

THINGSBOARD_HOST = 'demo.thingsboard.io' 
ACCESS_TOKEN_HC = 'WJUNtDkejLyn9nKhgDov'
ACCESS_TOKEN_DHT = 'LD3XPkG3Q4hgCaVqXrBs'

# Data capture and upload interval in seconds. Less interval will eventually.
INTERVAL = 1

sensor_data = {'distance': 0} 
next_reading = time.time() 

# client
client_hc = mqtt.Client()
client_dht = mqtt.Client()

# Set access token
client_hc.username_pw_set(ACCESS_TOKEN_HC)
client_dht.username_pw_set(ACCESS_TOKEN_DHT)


# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client_hc.connect(THINGSBOARD_HOST, 1883, 60) 
client_dht.connect(THINGSBOARD_HOST, 1883, 60) 

client_hc.loop_start()
client_dht.loop_start()



def distance():

    # set Trigger to HIGH
    
    GPIO.output(GPIO_TRIGGER, True)
    print("set trig true done")
    # set Trigger after 0.01ms to LOW 
    time.sleep(0.00001) 
    GPIO.output(GPIO_TRIGGER, False) 
    StartTime = time.time()
    StopTime = time.time()  # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival 
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s) # and divide by 2, because there and back 
    distance = (TimeElapsed * 34300) / 2
    return distance


if name == '  main  ':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist) 
            sensor_data['distance'] = dist 
            client_hc.publish('v1/devices/me/telemetry',json.dumps(sensor_data), 1)
            client_dht.publish('v1/devices/me/telemetry',json.dumps(sensor_data), 1)
            next_reading += INTERVAL
            sleep_time = next_reading-time.time() 
        if sleep_time > 0:
            time.sleep(sleep_time)
    
    # Reset by pressing CTRL + C 
    except KeyboardInterrupt:
        print("Measurement stopped by User") 
        GPIO.cleanup()

client_hc.loop_stop() 
client_dht.loop_stop() 

client_hc.disconnect()
client_dht.disconnect()


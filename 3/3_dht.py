# Libraries import os import time import sys
import paho.mqtt.client as mqtt 
import json
import RPi.GPIO as GPIO 
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)  # set GPIO Pins 
GPIO_DATA = 4

# set GPIO direction (IN / OUT) 
GPIO.setup(GPIO_DATA, GPIO.IN) 


THINGSBOARD_HOST = 'demo.thingsboard.io' 
ACCESS_TOKEN = 'LD3XPkG3Q4hgCaVqXrBs'

# Data capture and upload interval in seconds. Less interval will eventually.
INTERVAL = 1

sensor_data = {'temperature': 0, 'humidity': 0}
next_reading = time.time() 
client = mqtt.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60) 
client.loop_start()




if __name__ == "__main__": 
    try:
        while True:
            humidity,temperature = dht.read_retry(dht.DHT22, 4)
            humidity = round(humidity, 2)
            temperature = round(temperature, 2)
            print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
            sensor_data['temperature'] = temperature
            sensor_data['humidity'] = humidity

            # Sending humidity and temperature data to ThingsBoard
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

            next_reading += INTERVAL
            sleep_time = next_reading-time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)
    
    # Reset by pressing CTRL + C 
    except KeyboardInterrupt:
        print("Measurement stopped by User") 
        GPIO.cleanup()

client.loop_stop() 
client.disconnect()

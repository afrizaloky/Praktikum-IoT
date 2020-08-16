from datetime import datetime
import json
import random
import struct
import os
import signal
import requests
import sys

# from local_database import * #from server_protocol import * from datetime import datetime

server_domain = 'https://demo.thingsboard.io/api/v1/'
token = 'balbala'
url_api_data = '/attributes'


def send_data_to_server():
    global response
    print('sending data...')

    url = server_domain + token + url_api_data
    headers = {'content-type': 'application/json'}
    payload = {
        "temperature"	: random.uniform(10.5, 100.5), "humidity"	: random.uniform(10.5, 100.5),
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.status_code)


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

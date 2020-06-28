import time
import logging
import os
import json

import urllib.request

import http.client


from grove.gpio import GPIO
import seeed_dht

def main():

    env = os.environ.get("ENVIRONMENT")
    interval = int(os.environ.get("INTERVAL", 10))
    api_key = os.environ.get("APIKEY")
    filepath = os.environ.get("FILEPATH", "data.csv")
    if api_key is None:
        raise ValueError("Environment variable APIKEY not found")

    if env is None:
        env = "development"

    if env == "development":
        logging.basicConfig(level=logging.DEBUG)
        http_logger = urllib.request.HTTPHandler(debuglevel=1)
        opener = urllib.request.build_opener(
            urllib.request.HTTPHandler(debuglevel=1),
            urllib.request.HTTPSHandler(debuglevel=1))
        urllib.request.install_opener(opener)
    elif env == "production":
        logging.basicConfig(level=logging.WARNING)
    else:
        raise ValueError("Environment variable ENVIRONMENT is development or production")

    sensor1 = seeed_dht.DHT("11", 5)
    sensor2 = seeed_dht.DHT("11", 22)
    sensor3 = GPIO(16, GPIO.IN)

    while True:
        ts = int(time.time())
        humi1, temp1 = sensor1.read()
        humi2, temp2 = sensor2.read()
        mag = sensor3.read()

        logging.info("timestamp {}".format(ts))
        logging.info('DHT{0}#1, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor1.dht_type, humi1, temp1))
        logging.info('DHT{0}#2, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor2.dht_type, humi2, temp2))
        logging.info("Magnetic {}".format(mag))


        data = json.dumps({
            "agent": "test",
            "metrics": [
                {
                    "name": "temperature_1",
                    "namespace": "Environment Sensor",
                    "data_point": {
                        "timestamp": ts,
                        "value": temp1
                    }
                },
                {
                    "name": "temperature_2",
                    "namespace": "Environment Sensor",
                    "data_point": {
                        "timestamp": ts,
                        "value": temp2
                    }
                },
                {
                    "name": "humidity_1",
                    "namespace": "Environment Sensor",
                    "data_point": {
                        "timestamp": ts,
                        "value": humi1
                    }
                },
                {
                    "name": "humidity_2", "namespace": "Environment Sensor",
                    "data_point": {
                        "timestamp": ts,
                        "value": humi2
                    }
                },
                {
                    "name": "Magnetic",
                    "namespace": "Environment Sensor",
                    "data_point": {
                        "timestamp": ts,
                        "value": mag
                    }
                }
            ]
        }, separators=(',', ':')).encode("UTF-8")
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(api_key)
        }
        logging.debug(data)
        logging.debug(headers)

        req = urllib.request.Request("https://gw.machinist.iij.jp/endpoint", data=data, headers=headers, method="POST")
        res = urllib.request.urlopen(req)
        logging.debug("response code is : {}".format(res.getcode()))
        logging.debug("response is : {}".format(res.read().decode("utf-8")))

        with open(filepath, "a") as f:
            f.write("{},{},{},{},{}\n".format(temp1, humi1, temp2, humi2, mag))

        time.sleep(interval)
if __name__ == '__main__':
    main()

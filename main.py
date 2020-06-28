import time
from grove.gpio import GPIO
import seeed_dht

def main():

    sensor1 = seeed_dht.DHT("11", 5)
    mag = GPIO(16, GPIO.IN)

    while True:
        humi, temp = sensor1.read()
        print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor1.dht_type, humi, temp))

        print("Magnetic", mag.read())
        time.sleep(1)

if __name__ == '__main__':
    main()

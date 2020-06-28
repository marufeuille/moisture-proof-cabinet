# Moisture Proof Cabinet with Raspi
- Sorry, this page is under writing.

## Motivation
- I used Dry box with [MD-3](http://www.toyoliving.co.jp/products-info-other/MD-3-1.html) for keep drying camera and supplies.
- MD-3 is desiccant which can refresh to plug in.
- But I often forget to refresh MD-3, so need to notify!!

## Requirements
### Software
- [Grove.py](https://github.com/Seeed-Studio/grove.py)

### Hardware
- [Grove DHT11](https://wiki.seeedstudio.com/Grove-TemperatureAndHumidity_Sensor/) x2
- [Grove Magnetic Switch](https://wiki.seeedstudio.com/Grove-Magnetic_Switch/)
- [Grove Base Hat for Raspberry Pi](https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html)
- Magnet (I bought [this one](https://www.amazon.co.jp/gp/product/B07ZGFT61B).)
- Raspberry Pi

### SaaS
- [Machinist](https://app.machinist.iij.jp/) for collect and visualize data.

## Usage
- set up your sensor.
- run command below.

```bash
. env.sh
python3 main.py
```

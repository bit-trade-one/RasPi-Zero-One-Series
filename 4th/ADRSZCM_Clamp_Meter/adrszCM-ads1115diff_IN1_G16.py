# Simple demo of reading the difference between channel 1 and 0 on an ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
# 来歴:　V00.01 2022/05/18 BTO Circuitpython用に変更

import time
import math
import board
import busio


# Import the ADS1x15 module.
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 16

# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()
ads = ADS.ADS1115(i2c, GAIN)

# Create single-ended input on channel 0
#chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

# Create differential input between channel 2 and 3
chan = AnalogIn(ads, ADS.P2, ADS.P3)

#print('Press Ctrl-C to quit...')
t_start = time.time()
#time.sleep(3.1)
#print(t_start)
# => 3.0999999046325684

num = 0
num_max = 500
sumI = 0
sqI = 0
sqrtI = 0
#while True:
while num < num_max:
    value = chan.voltage
    # print(value)
    sumI += value
    sqI  += (value * value)
    num += 1
t_end = time.time()
#print('t_end=',t_end)
#print('t_end - t_start=',t_end - t_start)
sumI = sumI/num_max
sqI = sqI/num_max

#print('sumI=: {0}'.format(sumI))
#print('sqI=: {0}'.format(sqI))
sqrtI = math.sqrt(sqI)
#print('sqrtI=: {0}'.format(sqrtI))
#print(sqrtI)
print(sqrtI * 20.0)             # 単位はA(アンペア）
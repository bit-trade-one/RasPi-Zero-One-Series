# Simple demo of reading the difference between channel 1 and 0 on an ADS1x15 ADC.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

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
    # Read the difference between channel 0 and 1 (i.e. channel 0 minus channel 1).
    # Note you can change the differential value to the following:
    #  - 0 = Channel 0 minus channel 1
    #  - 1 = Channel 0 minus channel 3
    #  - 2 = Channel 1 minus channel 3
    #  - 3 = Channel 2 minus channel 3
    #value = adc.read_adc_difference(0, gain=GAIN)
    #value = adc.read_adc_difference(2, gain=GAIN)
    value = adc.read_adc_difference(3, gain=GAIN)

    #value = adc.read_adc_difference(2, gain=GAIN)
    # Note you can also pass an optional data_rate parameter above, see
    # simpletest.py and the read_adc function for more information.
    # Value will be a signed 12 or 16 bit integer value (depending on the ADC
    # precision, ADS1015 = 12-bit or ADS1115 = 16-bit).
    #print('Channel 0 minus 1: {0}'.format(value))
    # Pause for half a second.
    #time.sleep(0.1)       
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
print(sqrtI)
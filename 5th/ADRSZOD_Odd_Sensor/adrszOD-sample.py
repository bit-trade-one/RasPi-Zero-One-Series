#!/usr/bin/env python
import smbus
import time
i2c = smbus.SMBus(1)
addr=0x68
#addr=0x6e

Vref=2.048

def swap16(x):
    return (((x << 8) & 0xFF00) |
        ((x >> 8) & 0x00FF))

def sign16(x):
    return ( -(x & 0b1000000000000000) |
        (x & 0b0111111111111111) )
#main
#while 1:
#i2c.write_byte(addr, 0b10011000) #16bit
i2c.write_byte(addr, 0b10011000) #16bit

time.sleep(0.2)
data = i2c.read_word_data(addr,0x00)
raw = swap16(int(hex(data),16))
raw_s = sign16(int(hex(raw),16))
volts1 = round((Vref * raw_s / 32767),5)

i2c.write_byte(addr, 0b10111000) #16bit
time.sleep(0.2)

data = i2c.read_word_data(addr,0x00)
raw = swap16(int(hex(data),16))
raw_s = sign16(int(hex(raw),16))
volts2 = round((Vref * raw_s / 32767),5)

i2c.write_byte(addr, 0b11011000) #16bit
time.sleep(0.2)

data = i2c.read_word_data(addr,0x00)
raw = swap16(int(hex(data),16))
raw_s = sign16(int(hex(raw),16))
volts3 = round((Vref * raw_s / 32767),5)

i2c.write_byte(addr, 0b11111000) #16bit
time.sleep(0.2)

data = i2c.read_word_data(addr,0x00)
raw = swap16(int(hex(data),16))
raw_s = sign16(int(hex(raw),16))
volts4 = round((Vref * raw_s / 32767),5)

#print ("ch1=" + str(volts1) +"V")
#print ("ch2=" + str(volts2) +"V")
#print ("ch3=" + str(volts3) +"V")
#print ("ch4=" + str(volts4) +"V")
#print ("ch1-4=" + str(volts1) +"V "+ str(volts2) +"V "+ str(volts3) +"V " + str(volts4) +"V ")
#print (str(volts1))
out_msg = r'{'
out_msg += r'"ch1":'
out_msg += str(volts1)
out_msg += r','
out_msg += r'"ch2":'
out_msg += str(volts2)
out_msg += r','
out_msg += r'"ch3":'
out_msg += str(volts3)
out_msg += r','
out_msg += r'"ch4":'
out_msg += str(volts4)
out_msg += r'}'
print(out_msg)

#time.sleep(1)

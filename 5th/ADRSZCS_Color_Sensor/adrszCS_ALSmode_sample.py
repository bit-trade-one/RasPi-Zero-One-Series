#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import signal

import smbus
import time

import json

i2c = smbus.SMBus(1)
# Address Define
ADDR = 0x53
#import GYRO
#GYRO_XOUT_H = 0x43
CS_DATA_IR_0 = 0x0a
CS_DATA_GREEN_0 = 0x0d
CS_DATA_RED_0 = 0x10
CS_DATA_BLUE_0 = 0x13
CS_DATA_IR_0 = 0x0a

MAIN_CTRL = 0x00
#bit2:cs_mode=1  ALS=0,bit1:cs_ensble=1 
#i2c.write_byte_data(ADDR,MAIN_CTRL,0x06)  #CS mode
i2c.write_byte_data(ADDR,MAIN_CTRL,0x02)   #als mode

if __name__ == "__main__":
	#signal.signal(signal.SIGINT,signal.SIG_DFL)
	#gyro = GYRO.GYRO()
	#time.sleep(0.1)
	#gyro.sensor_calib()
	#prev = time.time()
	#while True:
		#now = time.time()
		#Sense_return = i2c.read_i2c_block_data(ADDR,CS_DATA_GREEN_0,2)
		Sense_return = i2c.read_i2c_block_data(ADDR,MAIN_CTRL,1)
		#print(Sense_return)	
		#partid 0x06
		Sense_return = i2c.read_i2c_block_data(ADDR,0x06,1)
		#print(Sense_return)	
		#main_status 0x07
		Sense_return = i2c.read_i2c_block_data(ADDR,0x07,1)
		#print(Sense_return)	
		time.sleep(0.1)
		Sense_return = i2c.read_i2c_block_data(ADDR,CS_DATA_GREEN_0,3)
		g_data = ((Sense_return[2]<<16) +(Sense_return[1]<<8) + Sense_return[0])
		#print(g_data)	
		Sense_return = i2c.read_i2c_block_data(ADDR,CS_DATA_RED_0,3)
		r_data = ((Sense_return[2]<<16) +(Sense_return[1]<<8) + Sense_return[0])
		#print(r_data)	
		Sense_return = i2c.read_i2c_block_data(ADDR,CS_DATA_BLUE_0,3)
		b_data = ((Sense_return[2]<<16) +(Sense_return[1]<<8) + Sense_return[0])
		#print(b_data)
		Sense_return = i2c.read_i2c_block_data(ADDR,CS_DATA_IR_0,3)
		ir_data = ((Sense_return[2]<<16) +(Sense_return[1]<<8) + Sense_return[0])
		#print(ir_data)

		#print(now-prev,end = ",")
		#for out in gyro.get_sense_value():
			#print(out,end=",")
		#print("")
		#prev = now
		#s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'
		#print(s)
		out_msg = r'{'
		out_msg += r'"g_data":'
		out_msg += str(g_data)
		out_msg += r','
		out_msg += r'"r_data":'
		out_msg += str(r_data)
		out_msg += r','
		out_msg += r'"b_data":'
		out_msg += str(b_data)
		out_msg += r','
		out_msg += r'"ir_data":'
		out_msg += str(ir_data)
		out_msg += r'}'
		print(out_msg)
		
		#print('b_data=',b_data)
		#time.sleep(3.0)

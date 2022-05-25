#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import signal

import smbus
import time

import json
import cv2
import numpy as np

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
#bit2:cs_mode=1,bit1:cs_ensble=1
i2c.write_byte_data(ADDR,MAIN_CTRL,0x06)

#print('cv2.version=',cv2.__version__)
g_norm = 1.0
r_norm = 1.0
b_norm = 1.0




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
		# 白い紙のＲＧＢ最大値、Ｒ：40000、Ｇ：60000、Ｂ：40000  紫（上のほうが）不定
		# 白い紙のＲＧＢ最大値、Ｒ：35000、Ｇ：60000、Ｂ：20000  赤　が不定
		# 白い紙のＲＧＢ最大値、Ｒ：35000、Ｇ：60000、Ｂ：30000  赤　が不定  
		# 白い紙のＲＧＢ最大値、Ｒ：40000、Ｇ：60000、Ｂ：35000  赤を紫にご認識
		
		
		r_norm = r_data/40000.0   #40000
		g_norm = g_data/60000.0   #60000
		b_norm = b_data/40000.0   #40000
		#print ('ｒ=', r_data,r_norm ,'g=', g_data,g_norm,'b=', b_data,b_norm) 
		hsv_bgr = np.uint8([[[b_norm*255,g_norm*255,r_norm*255 ]]])
		hsv_data = cv2.cvtColor(hsv_bgr,cv2.COLOR_BGR2HSV)
		#print (hsv_data) 
		#print ('H=',hsv_data[0][0][0],'S=',hsv_data[0][0][1],'V=',hsv_data[0][0][2]) 
		h_data = 1.0
		h_data = hsv_data[0][0][0]
		s_data = hsv_data[0][0][1]
		v_data = hsv_data[0][0][2]
		#print (h_data)
		
		#print (hsv_data[0],hsv_data[1],hsv_data[2]) 



		#green = np.uint8([[[0,255,0 ]]])
		#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
		#print hsv_green 

		#print(now-prev,end = ",")
		#for out in gyro.get_sense_value():
			#print(out,end=",")
		#print("")
		#prev = now
		#s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'
		#print(s)
		#out_msg = r'{' + r'"g_data":'+ str(g_data) + r',' + r'"r_data":' + str(r_data) + r','
		#out_msg += r'"b_data":' + str(b_data) + r',' + r'"ir_data":' + str(ir_data) + r'}'
		#print(out_msg)
		#out_msg = r'{' + r'"g_norm":'+ str(g_norm) + r',' + r'"r_norm":' + str(r_norm) + r','
		#out_msg += r'"b_norm":' + str(b_norm)  + r'}'
		#print(out_msg)
		out_msg = r'{' + r'"H":'+ str(h_data) + r',' + r'"S":' + str(s_data) + r','
		out_msg += r'"V":' + str(v_data)  + r'}'
		print(out_msg)



		#print('b_data=',b_data)
		#time.sleep(3.0)

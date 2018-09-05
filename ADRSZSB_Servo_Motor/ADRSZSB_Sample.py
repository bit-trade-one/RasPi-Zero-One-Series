#!/usr/bin/env python3
# coding: utf-8

import signal
import SVO
from time import sleep

if __name__ == "__main__":
	signal.signal(signal.SIGINT,signal.SIG_DFL)
	svo =SVO.SVO()
	while True:
		print()
		cmd = input("input command D(duty)/ a(all ch)/ c(cycle)/ x(max)/ n(min)/ r(Request)/ s(switch)/ q(QUIT):")

		if cmd == "d" or cmd == "D" or cmd =="":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				svo.Set_servo_duty(input("Channel(1/2/b(Both)):"),input("value:"))
			elif r_w == "r" or r_w == "R" or r_w =="":
				print(svo.Get_servo_duty(input("Channel(1/2):")))
			else:
				print("invalid command")

		elif cmd == "a" or cmd == "A":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				ch1_val = input("CH1 Duty :")
				ch2_val = input("CH2 Duty :")
				svo.Set_servo_duty_isolate(ch1_val,ch2_val)
			elif r_w == "r" or r_w == "R" or r_w =="":
				svo.Get_servo_duty_isolate()

		elif cmd == "C" or cmd == "c":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				svo.Set_servo_cycle(input("value:"))
			elif r_w == "r" or r_w == "R" or r_w == "":
				print(svo.Get_servo_cycle())
			else:
				print("invalid command")


		elif cmd == "X" or cmd == "x":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				svo.Set_servo_duty_max(input("Channel(1/2/b(Both)):"),input("value:"))
			elif r_w == "r" or r_w == "R" or r_w == "":
				print(svo.Get_servo_duty_max(input("Channel(1/2)):")))
			else:
				print("invalid command")


		elif cmd == "N" or cmd == "n":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				svo.Set_servo_duty_min(input("Channel(1/2/b(Both)):"),input("value:"))
			elif r_w == "r" or r_w == "R" or r_w == "":
				print(svo.Get_servo_duty_min(input("Channel(1/2)):")))
			else:
				print("invalid command")


		elif cmd == "S" or cmd == "s":
			r_w = input("Read/Write(R/w):")
			if r_w == "w" or r_w == "W":
				svo.Servo_Switch(input("Channel(1/2/b(Both)):"),input("1(ON)/0(OFF):"))
			elif r_w == "r" or r_w == "R" or r_w == "":
				print(0x01 & svo.Get_servo_state(input("Channel(1/2):")))
			else:
				print("invalid command")


		elif cmd == "R" or cmd == "r":
			svo.Set_servo_Write()

		elif cmd == "q" or cmd == "Q":
			print("Quit.")
			exit()

		else:
			print("invalid command")

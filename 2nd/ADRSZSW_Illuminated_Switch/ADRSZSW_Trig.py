#!/usr/bin/env python3
# - coding: utf-8 -
#
# ビット・トレード・ワン社提供のzerooneシリーズ 照光スイッチ(型番：ADRSZSW)用の例題プログラム
#　著作権者:(C) 2015 ビット・トレード・ワン社
#　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： ./ADRSZSW_OneShot.py
#  実行すると、スイッチを押すごとに入力状態とランプが切り替わります。
#  また、1秒ごとにスイッチの入力状態とランプの光度(0~255)を表示します。

import RPi.GPIO as GPIO
import smbus
import signal
import threading
from time import sleep

ADDR = 0x56
SW = 5

Switch_Flag = False


def switch():
	ON_Count = 0
	OFF_Count = 0
	global Switch_Flag
	while True:
		if GPIO.input(SW):
			OFF_Count = 0
			ON_Count +=1
		else:
			ON_Count = 0
			OFF_Count += 1

		if ON_Count == 10:
			Switch_Flag = not Switch_Flag
			i2c.write_byte_data(ADDR,0x01,int(Switch_Flag) * 255)

		sleep(0.001)

if __name__ == "__main__":
	signal.signal(signal.SIGINT,signal.SIG_DFL)

	i2c = smbus.SMBus(1)
	i2c.write_byte_data(ADDR,0x01,0)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(SW,GPIO.IN)

	switch_thread = threading.Thread(target=switch)
	switch_thread.start()

	while True:
		sleep(1)
		print(i2c.read_byte_data(ADDR,0x00))
		print(Switch_Flag)

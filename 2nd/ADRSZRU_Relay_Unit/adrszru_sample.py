#!/usr/bin/env python3
# coding: utf-8
#
# ファイル名：adrszru_sample.py
# バージョン：2018/07/30 v1.0  python3用
#
# ビット・トレード・ワン社提供の「ゼロワン」シリーズ リレー基板(型番：ADRSZRU)用の例題プログラム
# 著作権者:(C) 2015 ビット・トレード・ワン社
# ライセンス: ADL(Assembly Desk License)
#
# 実行方法： ./adrszru_sample.py
# 実行するとリレーが0.5秒ごとにONとOFFを繰り返します。

port = 4
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port, GPIO.OUT)
while 1:
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(port, GPIO.LOW)
    time.sleep(0.5)
GPIO.cleanup()

#!/usr/bin/env python3
#coding: utf-8
#####!で始まる1行目の記述はShebangスクリプト自体を実行
#####2行目に、マジックコメントを記述文字エンコーディング
#
#
# ファイル名：adrszSN_sample.py
# バージョン：2018/6/20 v1.0  python3用
#          
#
# ビット・トレード・ワン社提供のzerooneシリーズ ソレノイドモジュール(型番：ADRSZSN)用の例題プログラム
#　著作権者:(C) 2015 ビット・トレード・ワン社
#　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： ./adrszSN_sample.py
#　実行すると　ソレノイドが0.5秒ＯＮになり2秒間隔で繰り返します。
#  
#　


port = 4
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.OUT)
while 1:
    GPIO.output(port, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(port, GPIO.LOW)
    time.sleep(1.5)
GPIO.cleanup()

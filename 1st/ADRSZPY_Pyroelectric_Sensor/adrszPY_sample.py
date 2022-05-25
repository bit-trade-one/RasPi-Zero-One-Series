#!/usr/bin/env python3
# coding: utf-8
#####!で始まる1行目の記述はShebangスクリプト自体を実行
#####2行目に、マジックコメントを記述文字エンコーディング
#
#
# ファイル名：adrszPY_sample.py
# バージョン：2018/6/20 v1.0  python3用
#
#
# ビット・トレード・ワン社提供のzerooneシリーズ 焦電センサモジュール(型番：ADRSZPY)用の例題プログラム
# 　著作権者:(C) 2015 ビット・トレード・ワン社
# 　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： ./adrszPY_sample.py
# 　実行すると　焦電センサの入力値を１秒間隔でコンソールに出力します。
#
#


port = 5
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(port, GPIO.IN)
while 1:
    print(GPIO.input(port))
    time.sleep(1.0)
GPIO.cleanup()

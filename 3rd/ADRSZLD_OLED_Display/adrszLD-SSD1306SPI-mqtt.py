#!/usr/bin/env python3
# coding: utf-8
#
# ファイル名：adrszLD-SSD1306SPI-mqtt.py
# バージョン：2018/10/10 v2.0
#
# ビット・トレード・ワン社提供の ラズパイＺＥＲＯＯＮＥシリーズ
# ＯＬＥＤ漢字表示基板(型番：ADRSZLD)用のツール
#　著作権者:(C) 2015 ビット・トレード・ワン社
#　ライセンス: ADL(Assembly Desk License)
#
#  実行方法：python3 ./adrszLD-SSD1306SPI-mqtt.py
# 　仕様
#　　　入力：localhostのＭＱＴＴブローカから、TOPIC：adrszLDで文字列入力
#           mqttc.connect("localhost", 1883, 60)
#           mqttc.subscribe("adrszLD",0)
#
#　　　出力：ＭＱＴＴで入力した文字列を、自動スクロール４行で表示
#
# 利用例：
#  mosquitto_pub -h localhost -t adrszLD -m "メッセージ"
#

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import paho.mqtt.client as mqtt

# MQTTの設定
MQTT_HOST = 'localhost'
MQTT_TOPIC = 'adrszLD'


# OLEDのサイズ設定
OLED_WIDTH = 128
OLED_HEIGHT = 64

# OLEDとSPIバスの設定
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# フォントの設定
DEFAULT_FONT = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE = 14


# TryeTypeフォントオブジェクト
jpfont = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')
# SPIオブジェクト
spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000)
# 128×64ドットのOLEDオブジェクト
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=spi)


# OLEDオブジェクトのスタート
disp.begin()

# OLEDオブジェクトのバッファークリア
disp.clear()
# バッファの表示
disp.display()

# Imageオブジェクトの作成
image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT) ,0)
# drawオブジェクトの取得
draw = ImageDraw.Draw(image)
# 文字列の設定
gyou = [ 'こんにちは',
         'ビット・トレード・ワン',
         'ラズパイzerooneシリーズ ',
         'adrszLD 漢字ボード  ' ]
# 文字をimageに描く
for i, j in enumerate(gyou):
    draw.text((0,16 * i), j, font=jpfont, fill=1)
# imageをOLEDバッファーに書き込む
disp.image(image)
# バッファーを表示
disp.display()


## MQTT

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    global gyou
    global jpfont
    global disp

    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    m = msg.payload.decode()
    print(m)

    gyou = ([m] + gyou)[:4]

    # Imageオブジェクトの作成
    image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT) ,0)
    # drawオブジェクトの取得
    draw = ImageDraw.Draw(image)
    # 文字をimageに描く
    for i, j in enumerate(gyou):
        draw.text((0,16 * i), j, font=jpfont, fill=1)
    # imageをOLEDバッファーに書き込む
    disp.image(image)
    # バッファーを表示
    disp.display()

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
# mqttc.on_log = on_log        # Uncomment to enable debug messages

mqttc.connect(MQTT_HOST, 1883, 60)
mqttc.subscribe(MQTT_TOPIC, 0)
print("Host : " + MQTT_HOST)
print("Topic: " + MQTT_TOPIC)

try:
    mqttc.loop_forever()
except KeyboardInterrupt:
    pass

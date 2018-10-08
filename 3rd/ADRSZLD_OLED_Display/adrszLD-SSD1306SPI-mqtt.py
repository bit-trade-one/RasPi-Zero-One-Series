#!/usr/bin/python3
# coding: utf-8
#####!で始まる1行目の記述はShebangスクリプト自体を実行
#####2行目に、マジックコメントを記述文字エンコーディング
#
# ファイル名：adrszLD-SSD1306SPI-mqtt.py  python3用
# バージョン：2018/8/31 v1.0
#
# ビット・トレード・ワン社提供の ラズハ゜イＺＥＲＯＯＮＥシリーズ
# ＯＬＥＤ漢字表示基板(型番：ADRSZILD)用のツール
#　著作権者:(C) 2015 ビット・トレード・ワン社
#　ライセンス: ADL(Assembly Desk License)
#  実行方法：読込　./adrszLD-SSD1306SPI-mqtt.py
# 　仕様
#　　　入力：localhostのＭＱＴＴブローカから、TOPIC：adrszLDで文字列入力
#           mqttc.connect("localhost", 1883, 60)
#           mqttc.subscribe("adrszLD",0)
#
#　　　出力：ＭＱＴＴで入力した文字列を、自動スクロール４行で表示
#
#
#


import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#
#sudo python3 setup.py  install
import paho.mqtt.client as mqtt
import json
gyou1 = 'gyou1  '
gyou2 = 'gyou2  '
gyou3 = 'gyou3  '
gyou4 = 'gyou4  '
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
#DEFAULT_FONT = '/home/pi/font/misakifont/misaki_gothic.ttf'

FONT_SIZE = 14


# In[27]:



def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))




def on_message(mqttc, obj, msg):
    global gyou1
    global gyou2
    global gyou3
    global gyou4

    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #print(str(msg.payload))
    r = msg.payload.decode()
    print(r)
    #r4 = 'init  '
    #print(gyou4)
    gyou4 = gyou3
    gyou3 = gyou2
    gyou2 = gyou1
    r0 = r
    print(r0)
    gyou1 = r0

    # 128×64ドットのOLEDオブジェクト
    # disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=spi)
    # OLEDオブジェクトのスタート
    # disp.begin()
    # OLEDオブジェクトのバッファークリア
    # disp.clear()
    # バッファの表示
    # disp.display()
    # Imageオブジェクトの作成
    image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT) ,0)
    # drawオブジェクトの取得
    draw = ImageDraw.Draw(image)

# 文字をimageに描く

    draw.text((0,0),gyou1, font=jpfont, fill=1)
    draw.text((0,16),gyou2, font=jpfont, fill=1)
    draw.text((0,32),gyou3, font=jpfont, fill=1)
    draw.text((0,48),gyou4, font=jpfont, fill=1)

    # imageをOLEDバッファーに書き込む
    disp.image(image)
    # バッファーを表示
    disp.display()
    #lcd_string(gyou1,LCD_LINE_1)
    #lcd_string(gyou2,LCD_LINE_2)
    #lcd_string(gyou3,LCD_LINE_3)
    #lcd_string(gyou4,LCD_LINE_4)

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)



# In[28]:


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

# TryeTypeフォントオブジェクト
jpfont = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')


# In[29]:



mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("localhost", 1883, 60)
#mqttc.subscribe("Out-ssd1306spi",0)
mqttc.subscribe("adrszLD",0)

mqttc.loop_start()





# In[30]:



# 文字をimageに描く
gyou1 = 'こんにちは'
gyou2 = 'ビット・トレード・ワン'
gyou3 = 'ラズハ゜イzerooneシリーズ '
gyou4 = 'adrszLD 漢字ボード  '
draw.text((0,0),gyou1, font=jpfont, fill=1)
draw.text((0,16),gyou2, font=jpfont, fill=1)
draw.text((0,32),gyou3, font=jpfont, fill=1)
draw.text((0,48),gyou4, font=jpfont, fill=1)

# imageをOLEDバッファーに書き込む
disp.image(image)
# バッファーを表示
disp.display()

def main():
  # Main program block
  #draw.text((0,0),gyou1, font=jpfont, fill=1)
  while True:
      #
      time.sleep(3)
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    # OLEDオブジェクトのバッファークリア
    disp.clear() #lcd_byte(0x01, LCD_CMD)

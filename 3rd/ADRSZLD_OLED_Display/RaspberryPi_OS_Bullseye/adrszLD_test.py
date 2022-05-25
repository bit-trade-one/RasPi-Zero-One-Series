#!/usr/bin/env python3
# coding: utf-8
#
# ファイル名：adrszLD_test.py
# バージョン：2022/04/06 v0.0
#
# ビット・トレード・ワン社提供の ラズパイＺＥＲＯＯＮＥシリーズ
# ＯＬＥＤ漢字表示基板(型番：ADRSZLD)用のツール
#　著作権者:(C) 2015 ビット・トレード・ワン社
#　ライセンス: ADL(Assembly Desk License)
#
#  実行方法：python3 ./adrszLD_test.py

import board
import adafruit_ssd1306
import digitalio

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# OLEDのサイズ設定
OLED_WIDTH   =  128
OLED_HEIGHT  =  64

# フォントの設定
DEFAULT_FONT  =  '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE     =  14

# TryeTypeフォントオブジェクト
jpfont = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

# SPIオブジェクト
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D8)
oled_reset = digitalio.DigitalInOut(board.D24)
oled_dc = digitalio.DigitalInOut(board.D23)

disp = adafruit_ssd1306.SSD1306_SPI(OLED_WIDTH, OLED_HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# OLEDオブジェクトのバッファークリア
disp.fill(0)

# バッファの表示
# disp.display()
disp.show()

# 文字列の設定
gyou = [ 'こんにちは',
         'ビット・トレード・ワン',
         'ラズパイzerooneシリーズ ',
         'adrszLD 漢字ボード  ' ]

def draw_gyou():
    global gyou
    global jpfont
    global disp

    # Imageオブジェクトの作成
    image = Image.new("1", (OLED_WIDTH, OLED_HEIGHT), 0)

    # drawオブジェクトの取得
    draw = ImageDraw.Draw(image)

    # 文字をimageに描く
    for i, j in enumerate(gyou):
        draw.text((0,16 * i), j, font=jpfont, fill=1)

    # imageをOLEDバッファーに書き込む
    disp.image(image)

    # バッファーを表示
    disp.show()

def main():
        draw_gyou()

if __name__ == "__main__":
    main()

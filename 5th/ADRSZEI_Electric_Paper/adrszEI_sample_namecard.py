#!/usr/bin/env python
### coding: UTF-8

import argparse
import sys

from PIL import Image, ImageFont, ImageDraw
import inky

inky_display_WIDTH = 250
inky_display_HEIGHT = 128



class InkyPHAT(inky.Inky):
    WIDTH = 250
    HEIGHT = 128
    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 2

    def __init__(self, colour):
        inky.Inky.__init__(self, resolution=(self.WIDTH, self.HEIGHT), colour=colour, h_flip=False, v_flip=False) 

parser = argparse.ArgumentParser(description='Usage:sudo python3 adrszEI_sample_namecard.py  （株）ビット・トレード・ワン 阿部')    # 2. パーサを作る
# 3. parser.add_argumentで受け取る引数を追加していく

parser.add_argument('arg1', help='1行目文字列')    # 必須の引数を追加
parser.add_argument('arg2', help='2行目文字列')    # 必須の引数を追加
"""
parser.add_argument('arg3', help='3行目文字列')    # 必須の引数を追加
parser.add_argument('arg4', help='4行目文字列')    # 必須の引数を追加
"""
args = parser.parse_args()    # 4. 引数を解析

text1 = u"1行目文字列"
text2 = u"2行目文字列"
text3 = u"3行目文字列"
text4 = u"4行目文字列"

text1 = args.arg1
text2 = args.arg2
"""
text3 = args.arg3
text4 = args.arg4
"""
print("""
Usage:sudo python3 adrszEI_sample_namecard.py  1行目文字列　2行目文字列　
Usage:sudo python3 adrszEI_sample_namecard.py  （株）ビット・トレード・ワン 阿部
注意：arg間は、半角スペース
""")
DEFAULT_FONT = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE = 11
font11 = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')
FONT_SIZE = 16
font16 = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')
FONT_SIZE = 22
font22 = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

FONT_SIZE = 28
font28 = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')
FONT_SIZE = 56
font56 = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

colour = "black"


inky_display = InkyPHAT(colour)
#inky.Inky.__init__(inky.Inky,resolution=(250, 128),colour='black', h_flip=False, v_flip=False)


scale_size = 1
padding = 0


img = Image.new("P", (inky_display_WIDTH, inky_display_HEIGHT))
#print(inky_display_WIDTH, inky_display_HEIGHT)


draw = ImageDraw.Draw(img)
#font = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

name = "01234567890123test"





draw.text((0,0),text1,font=font22,fill=1)

draw.text((50,50),text2,font=font56,fill=1)
#draw.text((0,60),text3,font=font,fill=1)
#draw.text((0,90),text4,font=font,fill=1)

img_rotate = img.rotate(180)

# Display the completed name badge
inky_display.set_image(img_rotate)
#inky.Inky.set_image(inky.Inky,img_rotate)

#Inky.set_image(img_rotate)
#inky.image(img_rotate)

#inky_display.set_image(image)
inky_display.show()
#inky.Inky.show(inky.Inky)

#inky.show()

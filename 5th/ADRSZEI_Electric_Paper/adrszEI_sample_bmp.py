#!/usr/bin/env python
### coding: UTF-8

import argparse

#from PIL import Image, ImageFont, ImageDraw
from PIL import Image, ImageFont, ImageDraw,ImageOps
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

parser = argparse.ArgumentParser(description='Usage:sudo python3 adrszEI_sample_bmp.py  bmpファイル名')    # 2. パーサを作る
# 3. parser.add_argumentで受け取る引数を追加していく
parser.add_argument('arg1', help='例：bto_250x128_inv.bmp、bmpファイル名 白黒逆転タイプ')    # 必須の引数を追加
args = parser.parse_args()    # 4. 引数を解析

print("""
Usage:sudo python3 adrszEI_sample_bmp.py bmpファイル名
""")


colour = "black"

#print(inky_display.WIDTH, inky_display.HEIGHT)
inky_display = InkyPHAT(colour)
#print(inky_display.WIDTH, inky_display.HEIGHT)

#inky_display = InkyPHAT(colour,resolution=(250, 122))

scale_size = 1
padding = 0


img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
#print(inky_display.WIDTH, inky_display.HEIGHT)
draw = ImageDraw.Draw(img)
#font = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')


#img = Image.open("/home/pi/zeroone/4_3adrszEI/3-line-250_122_sample/checker_3-1.bmp")
#img = Image.open("/home/pi/zeroone/4_3adrszEI/3-line-250_122_sample/bto_250x128.bmp")
#img = Image.open("/home/pi/zeroone/4_3adrszEI/3-line-250_122_sample/bto_250x128_inv.bmp")
img = Image.open(args.arg1)

img_rotate = img.rotate(180)
#img_invert =  ImageOps.invert(img_rotate)

# Display the completed name badge
inky_display.set_image(img_rotate)
#inky_display.set_image(img_invert)

#inky_display.set_image(image)
inky_display.show()

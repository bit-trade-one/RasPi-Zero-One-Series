#!/usr/bin/env python
### coding: UTF-8

import argparse

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



print("""
Usage:sudo python3 adrszEI_3L_sample_test.py
""")
DEFAULT_FONT = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE = 28
font = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

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

text1 = u"_試験12月19日"
text2 = u"_試験15時00分"
text3 = u"_adrszEI_e-ink"
text4 = u"012345678901234567890"



draw.text((0,0),text1,font=font,fill=1)
draw.text((0,30),text2,font=font,fill=1)
draw.text((0,60),text3,font=font,fill=1)
draw.text((0,90),text4,font=font,fill=1)

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

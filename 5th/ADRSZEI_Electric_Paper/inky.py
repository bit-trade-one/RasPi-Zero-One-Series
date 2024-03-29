import sys
import time
import struct

import spidev

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

try:
    import RPi.GPIO as GPIO
except ImportError:
    sys.exit("This library requires the RPi.GPIO module\nInstall with: sudo pip install RPi.GPIO")

try:
    import numpy
except ImportError:
    sys.exit("This library requires the numpy module\nInstall with: sudo pip install numpy")


#inky_display.WIDTH = 250
#inky_display.HEIGHT = 128
#inky.WIDTH = 250
#inky.HEIGHT = 128


WHITE = 0
BLACK = 1
RED = YELLOW = 2

#RESET_PIN = 27
#BUSY_PIN = 17
#DC_PIN = 22
RESET_PIN = 17
BUSY_PIN = 24
DC_PIN = 25

MOSI_PIN = 10
SCLK_PIN = 11
CS0_PIN = 0

_SPI_CHUNK_SIZE = 4096
_SPI_COMMAND = GPIO.LOW
_SPI_DATA = GPIO.HIGH

_RESOLUTION = {
    (400, 300): (400, 300, 0),
    #(212, 104): (104, 212, -90),
    #(250, 122): (122, 250, -90),
    #(250, 120): (120, 250, -90),
    
    #(250, 104): (104, 250, -90),
    (250, 128): (128, 250, -90),
    

}


class Inky:
    DEFAULT_FONT = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
    FONT_SIZE = 14
    _LINE_HEIGHT = 16
    WIDTH = 250
    HEIGHT = 128

    #def __init__(self, resolution=(400, 300), colour='black', cs_pin=CS0_PIN, dc_pin=DC_PIN, reset_pin=RESET_PIN, busy_pin=BUSY_PIN, h_flip=False, v_flip=False):
    def __init__(self, resolution=(250, 128), colour='black', cs_pin=CS0_PIN, dc_pin=DC_PIN, reset_pin=RESET_PIN, busy_pin=BUSY_PIN, h_flip=False, v_flip=False):
    
        if resolution not in _RESOLUTION.keys():
            raise ValueError("Resolution {}x{} not supported!".format(*resolution))

        self.resolution = resolution
        self.width, self.height = resolution
        self.cols, self.rows, self.rotation = _RESOLUTION[resolution]

        if colour not in ('red', 'black', 'yellow'):
            raise ValueError("Colour {} is not supported!".format(colour))

        self.colour = colour

        self.buf = numpy.zeros((self.height, self.width), dtype=numpy.uint8)
        self.border_colour = 0

        self.dc_pin = dc_pin
        self.reset_pin = reset_pin
        self.busy_pin = busy_pin
        self.cs_pin = cs_pin
        self.h_flip = h_flip
        self.v_flip = v_flip

        self._gpio_setup = False

        self._image = Image.new('1', (self.WIDTH, self.HEIGHT) ,0)
        self._draw = ImageDraw.Draw(self._image)
        self._font = ImageFont.truetype(self.DEFAULT_FONT, self.FONT_SIZE, encoding='unic')


        self._luts = {
            'black': [
            # Phase 0     Phase 1     Phase 2     Phase 3     Phase 4     Phase 5     Phase 6
            # A B C D     A B C D     A B C D     A B C D     A B C D     A B C D     A B C D
            0b01001000, 0b10100000, 0b00010000, 0b00010000, 0b00010011, 0b00000000, 0b00000000,  # LUT0 - Black
            0b01001000, 0b10100000, 0b10000000, 0b00000000, 0b00000011, 0b00000000, 0b00000000,  # LUTT1 - White
            0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,  # IGNORE
            0b01001000, 0b10100101, 0b00000000, 0b10111011, 0b00000000, 0b00000000, 0b00000000,  # LUT3 - Red
            0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,  # LUT4 - VCOM

            # Duration            |  Repeat
            # A   B     C     D   |
            16,   4,    4,    4,     4,   # 0 Flash
            16,   4,    4,    4,     4,   # 1 clear
            4,    8,    8,    16,    16,  # 2 bring in the black
            0,    0,    0,    0,     0,   # 3 time for red
            0,    0,    0,    0,     0,   # 4 final black sharpen phase
            0,    0,    0,    0,     0,   # 5
            0,    0,    0,    0,     0,   # 6
            ],
            'red': [
            # Phase 0     Phase 1     Phase 2     Phase 3     Phase 4     Phase 5     Phase 6
            # A B C D     A B C D     A B C D     A B C D     A B C D     A B C D     A B C D
            0b01001000, 0b10100000, 0b00010000, 0b00010000, 0b00010011, 0b00000000, 0b00000000,  # LUT0 - Black
            0b01001000, 0b10100000, 0b10000000, 0b00000000, 0b00000011, 0b00000000, 0b00000000,  # LUTT1 - White
            0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,  # IGNORE
            0b01001000, 0b10100101, 0b00000000, 0b10111011, 0b00000000, 0b00000000, 0b00000000,  # LUT3 - Red
            0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000,  # LUT4 - VCOM

            # Duration            |  Repeat
            # A   B     C     D   |
            64,   12,   32,   12,    6,   # 0 Flash
            16,   8,    4,    4,     6,   # 1 clear
            4,    8,    8,    16,    16,  # 2 bring in the black
            2,    2,    2,    64,    32,  # 3 time for red
            2,    2,    2,    2,     2,   # 4 final black sharpen phase
            0,    0,    0,    0,     0,   # 5
            0,    0,    0,    0,     0    # 6
            ],
            'yellow': [
            # Phase 0     Phase 1     Phase 2     Phase 3     Phase 4     Phase 5     Phase 6
            # A B C D     A B C D     A B C D     A B C D     A B C D     A B C D     A B C D
            0b11111010, 0b10010100, 0b10001100, 0b11000000, 0b11010000,  0b00000000, 0b00000000,  # LUT0 - Black
            0b11111010, 0b10010100, 0b00101100, 0b10000000, 0b11100000,  0b00000000, 0b00000000,  # LUTT1 - White
            0b11111010, 0b00000000, 0b00000000, 0b00000000, 0b00000000,  0b00000000, 0b00000000,  # IGNORE
            0b11111010, 0b10010100, 0b11111000, 0b10000000, 0b01010000,  0b00000000, 0b11001100,  # LUT3 - Yellow (or Red)
            0b10111111, 0b01011000, 0b11111100, 0b10000000, 0b11010000,  0b00000000, 0b00010001,  # LUT4 - VCOM

            # Duration            | Repeat
            # A   B     C     D   |
            64,   16,   64,   16,   8,
            8,    16,   4,    4,    16,
            8,    8,    3,    8,    32,
            8,    4,    0,    0,    16,
            16,   8,    8,    0,    32,
            0,    0,    0,    0,    0,
            0,    0,    0,    0,    0,
            ]
        }

    def setup(self):
        if not self._gpio_setup:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.dc_pin, GPIO.OUT, initial=GPIO.LOW, pull_up_down=GPIO.PUD_OFF)
            GPIO.setup(self.reset_pin, GPIO.OUT, initial=GPIO.HIGH, pull_up_down=GPIO.PUD_OFF)
            GPIO.setup(self.busy_pin, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

            self._spi = spidev.SpiDev()
            self._spi.open(0, self.cs_pin)
            self._spi.max_speed_hz = 488000

            self._gpio_setup = True

        GPIO.output(self.reset_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.reset_pin, GPIO.HIGH)
        time.sleep(0.1)

        self._send_command(0x12)  # Soft Reset
        self._busy_wait()

    def _busy_wait(self):
        while(GPIO.input(self.busy_pin) != GPIO.LOW):
            time.sleep(0.01)

    def _update(self, buf_a, buf_b):
        self.setup()

        packed_height = list(struct.pack("<H", self.rows))

        if isinstance(packed_height[0], str):
            packed_height = map(ord, packed_height)

        #self._send_command(0x74, 0x54)  # Set Analog Block Control
        #self._send_command(0x7e, 0x3b)  # Set Digital Block Control

        #self._send_command(0x01, packed_height + [0x00])  # Gate setting
        self._send_command(0x01, [0xf9,0x00])  # Gate setting  for GDEH0213 cmd=1
        
        #print(packed_height + [0x00])

        self._send_command(0x03, [0b10000, 0b0001])  # Gate Driving Voltage

        #self._send_command(0x3a, 0x07)  # Dummy line period
        self._send_command(0x3a, 0x06)  # Dummy line period for GDEH0213 cmd=16
        
        #self._send_command(0x3b, 0x04)  # Gate line width
        self._send_command(0x3b, 0x0b)  # Gate line width for GDEH0213 cmd=17
        
        self._send_command(0x11, 0x03)  # Data entry mode setting 0x03 = X/Y increment
        #                                                   for GDEH0213 cmd=5

        #self._send_command(0x04)  # Power On
        self._send_command(0x04,0x19)  # Set Source output voltage 19h for GDEH0213 cmd=3
        
        self._send_command(0x2c, 0x3c)  # VCOM Register, 0x3c = -1.5v?-1.1v for GDEH0213 cmd=13


        self._send_command(0x3c, 0x00)  # white VCOM Register for GDEH0213 cmd=18
        if self.border_colour == self.BLACK:
            self._send_command(0x3c, 0x00)
        elif self.border_colour == self.RED:
            self._send_command(0x3c, 0x33)
        elif self.border_colour == self.YELLOW:
            self._send_command(0x3c, 0x33)
        elif self.border_colour == self.WHITE:
            self._send_command(0x3c, 0xFF)

        if self.colour == 'yellow':
            self._send_command(0x04, 0x07)  # Set voltage of VSH and VSL

        self._send_command(0x32, self._luts[self.colour])  # Set LUTs

        #self._send_command(0x44, [0x00, (self.cols // 8) - 1])  # Set RAM X Start/End
        #self._send_command(0x44, [0x00, 0x0b])  # Set RAM X Start/End  for GDEH0213 cmd=19
        #self._send_command(0x44, [0x00, 0x0c])  # Set RAM X Start/End  for GDEH0213 cmd=19 250*104 ok
        #self._send_command(0x44, [0x00, 0x0d])  # Set RAM X Start/End  for GDEH0213 cmd=19
        #self._send_command(0x44, [0x00, 0x0e])  # Set RAM X Start/End
        self._send_command(0x44, [0x00, 0x0f])  # Set RAM X Start/End
        
        #self._send_command(0x44, [0x00, 0x10])  # Set RAM X Start/End  for GDEH0213 cmd=19
        #self._send_command(0x44, [0x00, 0x12])  # Set RAM X Start/End  for GDEH0213 cmd=19
        #self._send_command(0x44, [0x00, 0x10])  # Set RAM X Start/End  for GDEH0213 cmd=19
        
        #print("self.cols=",self.cols)
        #print("(self.cols // 8) - 1=",(self.cols // 8) - 1)
        #print("str(0x12)=",str(0x12),"str(0x10)=",str(0x10),"str(0x0e)=",str(0x0e))

        #self._send_command(0x45, [0x00, 0x00] + packed_height)  # Set RAM Y Start/End
        self._send_command(0x45, [0x00, 0xf9] )  # Set RAM Y Start/End
        #print("packed_height=", packed_height)
        #print(" [0x00, 0x00] + packed_height=", [0x00, 0x00] + packed_height)
        #print("str(0xf9)=",str(0xf9))
        # 0x24 == RAM B/W, 0x26 == RAM Red/Yellow/etc

        #print("(0x24, buf_a)=",(0x24, buf_a))
        #print("(0x26, buf_b)=",(0x26, buf_b))
        for data in ((0x24, buf_a), (0x26, buf_b)):
        #for data in (0x24, buf_a):
            
            cmd, buf = data
            self._send_command(0x4e, 0x00)  # Set RAM X Pointer Start
            self._send_command(0x4f, [0x00, 0x00])  # Set RAM Y Pointer Start
            self._send_command(cmd, buf)

        self._send_command(0x22, 0xc7)  # Display Update Sequence
        self._send_command(0x20)  # Trigger Display Update
        time.sleep(0.05)
        self._busy_wait()
        self._send_command(0x10, 0x01)  # Enter Deep Sleep

    def set_pixel(self, x, y, v):
        if v in (WHITE, BLACK, RED):
            self.buf[y][x] = v

    def show(self):
        region = self.buf

        if self.v_flip:
            region = numpy.fliplr(region)

        if self.h_flip:
            region = numpy.flipud(region)

        if self.rotation:
            region = numpy.rot90(region, self.rotation // 90)

        buf_a = numpy.packbits(numpy.where(region == BLACK, 0, 1)).tolist()
        buf_b = numpy.packbits(numpy.where(region == RED, 1, 0)).tolist()
        #buf_b = numpy.packbits(numpy.where(region == BLACK, 0, 1)).tolist()

        self._update(buf_a, buf_b)
        #self._update(buf_a,buf_a)


    def set_border(self, colour):
        """Set the border colour."""
        if colour in (WHITE, BLACK, RED):
            self.border_colour = colour

    def set_image(self, image):
        """Copy an image to the display."""
        if self.rotation % 180 == 0:
            self.buf = numpy.array(image, dtype=numpy.uint8).reshape((self.width, self.height))
        else:
            self.buf = numpy.array(image, dtype=numpy.uint8).reshape((self.height, self.width))

    def _spi_write(self, dc, values):
        GPIO.output(self.dc_pin, dc)
        try:
            self._spi.xfer3(values)
        except AttributeError:
            for x in range(((len(values) - 1) // _SPI_CHUNK_SIZE) + 1):
                offset = x * _SPI_CHUNK_SIZE
                self._spi.xfer(values[offset:offset + _SPI_CHUNK_SIZE])

    def _send_command(self, command, data=None):
        self._spi_write(_SPI_COMMAND, [command])
        if data is not None:
            self._send_data(data)

    def _send_data(self, data):
        if isinstance(data, int):
            data = [data]
        self._spi_write(_SPI_DATA, data)

    def image(self, image):
        self._image = image
        #super().image(self._image)

    def drawString(self, str, line=0):
        self._draw.rectangle((0, line*self._LINE_HEIGHT, self.WIDTH,line*self._LINE_HEIGHT+self._LINE_HEIGHT), fill=(0))
        self._draw.text((0, line*self._LINE_HEIGHT), str, font=self._font, fill=1)
        #self.image(self._image)
    


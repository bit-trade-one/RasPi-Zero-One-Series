#!/usr/bin/env python3
# coding: utf-8

import smbus
import struct
import signal
from time import sleep

i2c = smbus.SMBus(1)
addr = 0x54

VALUE_HI = 0x00
VALUE_LO = 0x01
RESET = 0x02


def Get_encoder_value():
    temp = i2c.read_word_data(addr, VALUE_HI)
    return struct.unpack(">H", struct.pack("<H", temp))[0]


def Encoder_Reset():
    i2c.write_byte_data(addr, RESET, True)
    print("clear value")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    while True:
        cmd = input("input command(V/r/q):")
        if cmd == "v" or cmd == "":
            print(struct.unpack(">h", struct.pack(">H", Get_encoder_value()))[0])
        elif cmd == "r":
            Encoder_Reset()
        elif cmd == "q":
            print("QUIT.")
            exit()
        else:
            print("invalid command")

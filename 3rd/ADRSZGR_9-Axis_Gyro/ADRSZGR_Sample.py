#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time
import GYRO

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gyro = GYRO.GYRO()
    time.sleep(0.1)
    gyro.sensor_calib()
    prev = time.time()
    while True:
        now = time.time()
        print(now - prev, end=",")
        for out in gyro.get_sense_value():
            print(out, end=",")
        print("")
        prev = now
        time.sleep(0.05)

import smbus
import threading
import struct
import time

i2c = smbus.SMBus(1)

# MPU9250 Address Define
ADDR = 0x68
WHO_AM_I = 0x75

INT_PIN_CFG = 0x37

ACCEL_CONFIG = 0x1C

ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40

TEMP_OUT_H = 0x41
TEMP_OUT_L = 0x42

GYRO_CONFIG = 0x1B

GYRO_XOUT_H = 0x43
GYRO_XOUT_L = 0x44
GYRO_YOUT_H = 0x45
GYRO_YOUT_L = 0x46
GYRO_ZOUT_H = 0x47
GYRO_ZOUT_L = 0x48

PWR_MGMT_1 = 0x6B

# MagMetor Address Define
MG_ADDR = 0x0C
MG_DEV_ID = 0x00

MG_HXL = 0x03
MG_HXH = 0x04
MG_HYL = 0x05
MG_HYH = 0x06
MG_HZL = 0x07
MG_HZH = 0x08

MG_CNTL1 = 0x0A


class GYRO:

    __INIT_FLAG = False

    # Sensing value data
    __ACCEL_Z = 0
    __ACCEL_Y = 0
    __ACCEL_X = 0
    __TEMP = 0
    __GYRO_X = 0
    __GYRO_Y = 0
    __GYRO_Z = 0
    __MAG_X = 0
    __MAG_Y = 0
    __MAG_Z = 0

    __GYRO_OFS_X = 0
    __GYRO_OFS_Y = 0
    __GYRO_OFS_Z = 0

    # Sensor Range data
    __ac_conf = 3
    __gr_conf = 3

    # calibration data
    __calib_x = 0
    __calib_y = 0
    __calib_z = 0

    def read_loop(self):
        while True:

            Sense_return = i2c.read_i2c_block_data(ADDR, ACCEL_XOUT_H, 14)
            self.__ACCEL_X = self.accel_conv((Sense_return[0] << 8) + Sense_return[1])
            self.__ACCEL_Y = self.accel_conv((Sense_return[2] << 8) + Sense_return[3])
            self.__ACCEL_Z = self.accel_conv((Sense_return[4] << 8) + Sense_return[5])
            self.__TEMP = (Sense_return[6] << 8) + Sense_return[7]
            self.__GYRO_X = (
                self.gyro_conv((Sense_return[8] << 8) + Sense_return[9])
                + self.__calib_x
            )
            self.__GYRO_Y = (
                self.gyro_conv((Sense_return[10] << 8) + Sense_return[11])
                + self.__calib_y
            )
            self.__GYRO_Z = (
                self.gyro_conv((Sense_return[12] << 8) + Sense_return[13])
                + self.__calib_z
            )
            Mg_Sense_return = i2c.read_i2c_block_data(MG_ADDR, MG_HXL, 7)
            self.__MAG_X = self.mag_conv((Mg_Sense_return[1] << 8) + Mg_Sense_return[0])
            self.__MAG_Y = self.mag_conv((Mg_Sense_return[3] << 8) + Mg_Sense_return[2])
            self.__MAG_Z = self.mag_conv((Mg_Sense_return[5] << 8) + Mg_Sense_return[4])
            time.sleep(0.05)

    def accel_conv(self, val):
        return (
            (struct.unpack("<h", struct.pack("<H", val))[0])
            * (2 ** (self.__ac_conf + 1))
            / 32768
        )

    def gyro_conv(self, val):
        return (
            (struct.unpack("<h", struct.pack("<H", val))[0])
            * 250
            * (2 ** self.__gr_conf)
            / 32768
        )

    def mag_conv(self, val):
        return (struct.unpack("<h", struct.pack("<H", val))[0]) * 4912 / 32760

    def get_sense_value(self):
        if self.__INIT_FLAG:
            return (
                self.__ACCEL_X,
                self.__ACCEL_Y,
                self.__ACCEL_Z,
                self.__GYRO_X,
                self.__GYRO_Y,
                self.__GYRO_Z,
                self.__MAG_X,
                self.__MAG_Y,
                self.__MAG_Z,
            )
        else:
            return None

    def sensor_calib(self, count=10):
        x_data = ()
        y_data = ()
        z_data = ()
        begin = time.time()
        now = begin
        print("10秒間、センサを動かさないでください")
        while (now - begin) < count:
            print("\rあと{0}秒".format(count - int(now - begin)), end="")
            now = time.time()
            Sense_return = i2c.read_i2c_block_data(ADDR, GYRO_XOUT_H, 6)
            x_data += (self.gyro_conv((Sense_return[0] << 8) + Sense_return[1]),)
            y_data += (self.gyro_conv((Sense_return[2] << 8) + Sense_return[3]),)
            z_data += (self.gyro_conv((Sense_return[4] << 8) + Sense_return[5]),)
            time.sleep(0.05)

        self.__calib_x = -1 * sum(x_data) / len(x_data)
        self.__calib_y = -1 * sum(y_data) / len(y_data)
        self.__calib_z = -1 * sum(z_data) / len(z_data)
        print("\nキャリブレーション終了")
        print(
            "X:{0}\tY:{1}\tZ:{2}\n".format(
                self.__calib_x, self.__calib_y, self.__calib_z
            )
        )

    def __init__(self, ac_conf=0x03, gr_conf=0x03):
        if ac_conf < 0 or ac_conf > 3 or gr_conf < 0 or gr_conf > 3:
            return

        self.__ac_conf = ac_conf
        self.__gr_conf = gr_conf

        if i2c.read_byte_data(ADDR, WHO_AM_I) != 0x73:
            return

        i2c.write_byte_data(ADDR, PWR_MGMT_1, 0x00)
        i2c.write_byte_data(ADDR, INT_PIN_CFG, 0x02)

        if i2c.read_byte_data(MG_ADDR, MG_DEV_ID) != 0x48:
            i2c.write_byte_data(ADDR, INT_PIN_CFG, 0x00)
            i2c.write_byte_data(ADDR, PWR_MGMT_1, 0xC0)
            return

        i2c.write_byte_data(MG_ADDR, MG_CNTL1, 0x16)

        i2c.write_byte_data(ADDR, ACCEL_CONFIG, self.__ac_conf << 3)
        i2c.write_byte_data(ADDR, GYRO_CONFIG, self.__gr_conf << 3)

        loop = threading.Thread(target=self.read_loop)
        loop.setDaemon(True)
        loop.start()
        self.__INIT_FLAG = True

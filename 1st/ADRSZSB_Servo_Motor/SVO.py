import smbus
import struct

i2c = smbus.SMBus(1)


class SVO:
    __addr = 0x52
    ON = "1"
    OFF = "0"

    GET_CH1_STATE = 0x00
    GET_CH2_STATE = 0x01

    GET_CH1_DUTY_HI = 0x02
    GET_CH1_DUTY_LO = 0x03
    GET_CH1_DUTY = GET_CH1_DUTY_HI

    GET_CH2_DUTY_HI = 0x04
    GET_CH2_DUTY_LO = 0x05
    GET_CH2_DUTY = GET_CH2_DUTY_HI

    GET_PWM_CYCL_HI = 0x06
    GET_PWM_CYCL_LO = 0x07
    GET_PWM_CYCL = GET_PWM_CYCL_HI

    GET_CH1_DUTY_MAX_HI = 0x08
    GET_CH1_DUTY_MAX_LO = 0x09
    GET_CH1_DUTY_MAX = GET_CH1_DUTY_MAX_HI

    GET_CH1_DUTY_MIN_HI = 0x0A
    GET_CH1_DUTY_MIN_LO = 0x0B
    GET_CH1_DUTY_MIN = GET_CH1_DUTY_MIN_HI

    GET_CH2_DUTY_MAX_HI = 0x0C
    GET_CH2_DUTY_MAX_LO = 0x0D
    GET_CH2_DUTY_MAX = GET_CH2_DUTY_MAX_HI

    GET_CH2_DUTY_MIN_HI = 0x0E
    GET_CH2_DUTY_MIN_LO = 0x0F
    GET_CH2_DUTY_MIN = GET_CH2_DUTY_MIN_HI

    CH1_CTRL = 0x10
    CH1_CTRL_MSK = 0x11
    CH2_CTRL = 0x12
    CH2_CTRL_MSK = 0x13

    CH1_DUTY_MAX_HI = 0x14
    CH1_DUTY_MAX_LO = 0x15
    CH1_DUTY_MAX = CH1_DUTY_MAX_HI
    CH1_DUTY_MIN_HI = 0x16
    CH1_DUTY_MIN_LO = 0x17
    CH1_DUTY_MIN = CH1_DUTY_MIN_HI

    CH2_DUTY_MAX_HI = 0x18
    CH2_DUTY_MAX_LO = 0x19
    CH2_DUTY_MAX = CH2_DUTY_MAX_HI
    CH2_DUTY_MIN_HI = 0x1A
    CH2_DUTY_MIN_LO = 0x1B
    CH2_DUTY_MIN = CH2_DUTY_MIN_HI

    PWM_CYCL_HI = 0x1C
    PWM_CYCL_LO = 0x1D
    PWM_CYCL = PWM_CYCL_HI

    CH1_DUTY_HI = 0x1E
    CH1_DUTY_LO = 0x1F
    CH1_DUTY = CH1_DUTY_HI
    CH2_DUTY_HI = 0x20
    CH2_DUTY_LO = 0x21
    CH2_DUTY = CH2_DUTY_HI

    REQ_SET_VAL = 0x22

    REQ_CH1_DUTY = 0x01
    REQ_CH2_DUTY = 0x02
    REQ_PWM_CYCL = 0x04
    REQ_CH1_DUTY_MAX = 0x10
    REQ_CH1_DUTY_MIN = 0x20
    REQ_CH2_DUTY_MAX = 0x40
    REQ_CH2_DUTY_MIN = 0x80
    REQ_ALL = 0xFF

    INIT_SVO_MAX = 2400
    INIT_SVO_MIN = 500
    INIT_SVO_CCL = 20000

    __req = 0x0

    def Servo_Switch(self, ch, sw_str):
        if sw_str == "0":
            switch = False
        else:
            switch = True

        if ch == "1":
            i2c.write_byte_data(self.__addr, self.CH1_CTRL, switch)
            i2c.write_byte_data(self.__addr, self.CH1_CTRL_MSK, 0x01)
        elif ch == "2":
            i2c.write_byte_data(self.__addr, self.CH2_CTRL, switch)
            i2c.write_byte_data(self.__addr, self.CH2_CTRL_MSK, 0x01)
        elif ch == "b":
            i2c.write_byte_data(self.__addr, self.CH1_CTRL, switch)
            i2c.write_byte_data(self.__addr, self.CH1_CTRL_MSK, 0x01)
            i2c.write_byte_data(self.__addr, self.CH2_CTRL, switch)
            i2c.write_byte_data(self.__addr, self.CH2_CTRL_MSK, 0x01)
        else:
            print("invalid command")
        if switch == True:
            if 0x02 & i2c.read_byte_data(self.__addr, self.GET_CH1_STATE) == 1:
                print("CH1 Setting False")
            if 0x02 & i2c.read_byte_data(self.__addr, self.GET_CH2_STATE) == 1:
                print("CH2 Setting False")

    def Get_servo_state(self, ch):
        if ch == "1":
            return 0x01 & i2c.read_byte_data(self.__addr, self.GET_CH1_STATE)
        elif ch == "2":
            return 0x01 & i2c.read_byte_data(self.__addr, self.GET_CH2_STATE)
        else:
            print("invalid command")

    # -------------------------------------------------------------------------------------------------------------------------------------

    def Get_servo_duty(self, ch):
        if ch == "1":
            return struct.unpack(
                ">H",
                struct.pack("<H", i2c.read_word_data(self.__addr, self.GET_CH1_DUTY)),
            )[0]
        elif ch == "2":
            return struct.unpack(
                ">H",
                struct.pack("<H", i2c.read_word_data(self.__addr, self.GET_CH2_DUTY)),
            )[0]
        else:
            print("invalid command")

    def Get_servo_duty_isolate(self):
        print(
            "CH1:{0}".format(
                struct.unpack(
                    ">H",
                    struct.pack(
                        "<H", i2c.read_word_data(self.__addr, self.GET_CH1_DUTY)
                    ),
                )[0]
            )
        )
        print(
            "CH2:{0}".format(
                struct.unpack(
                    ">H",
                    struct.pack(
                        "<H", i2c.read_word_data(self.__addr, self.GET_CH2_DUTY)
                    ),
                )[0]
            )
        )

    def Get_servo_duty_max(self, ch):
        if ch == "1":
            return struct.unpack(
                ">H",
                struct.pack(
                    "<H", i2c.read_word_data(self.__addr, self.GET_CH1_DUTY_MAX)
                ),
            )[0]
        elif ch == "2":
            return struct.unpack(
                ">H",
                struct.pack(
                    "<H", i2c.read_word_data(self.__addr, self.GET_CH2_DUTY_MAX)
                ),
            )[0]
        else:
            print("invalid command")

    def Get_servo_duty_min(self, ch):
        if ch == "1":
            return struct.unpack(
                ">H",
                struct.pack(
                    "<H", i2c.read_word_data(self.__addr, self.GET_CH1_DUTY_MIN)
                ),
            )[0]
        elif ch == "2":
            return struct.unpack(
                ">H",
                struct.pack(
                    "<H", i2c.read_word_data(self.__addr, self.GET_CH2_DUTY_MIN)
                ),
            )[0]
        else:
            print("invalid command")

    def Get_servo_cycle(self):
        return struct.unpack(
            ">H", struct.pack("<H", i2c.read_word_data(self.__addr, self.GET_PWM_CYCL))
        )[0]

    # -------------------------------------------------------------------------------------------------------------------------------------

    def Set_servo_duty(self, ch, val_str):
        val = struct.unpack(">H", struct.pack("<H", int(val_str)))[0]
        if ch == "1":
            i2c.write_word_data(self.__addr, self.CH1_DUTY, val)
            self.__req |= self.REQ_CH1_DUTY
        elif ch == "2":
            i2c.write_word_data(self.__addr, self.CH2_DUTY, val)
            self.__req |= self.REQ_CH2_DUTY
        elif ch == "b":
            i2c.write_word_data(self.__addr, self.CH1_DUTY, val)
            i2c.write_word_data(self.__addr, self.CH2_DUTY, val)
            self.__req |= self.REQ_CH1_DUTY | self.REQ_CH2_DUTY
        else:
            print("invalid command")

    def Set_servo_duty_isolate(self, ch1_val_str, ch2_val_str):
        ch1_val = int(ch1_val_str)
        ch2_val = int(ch2_val_str)
        i2c.write_i2c_block_data(
            self.__addr,
            self.CH1_DUTY,
            [
                (ch1_val // 0x100),
                (ch1_val % 0x100),
                (ch2_val // 0x100),
                (ch2_val % 0x100),
                0x03,
            ],
        )

    def Set_servo_duty_max(self, ch, val_str):
        val = struct.unpack(">H", struct.pack("<H", int(val_str)))[0]
        if ch == "1":
            i2c.write_word_data(self.__addr, self.CH1_DUTY_MAX, val)
            self.__req |= self.REQ_CH1_DUTY_MAX
            if self.Get_servo_state(ch) == 1:
                print("Please turn off CH1 POWER.")
        elif ch == "2":
            i2c.write_word_data(self.__addr, self.CH2_DUTY_MAX, val)
            self.__req |= self.REQ_CH2_DUTY_MAX
            if self.Get_servo_state(ch) == 1:
                print("Please turn off CH2 POWER.")
        elif ch == "b":
            i2c.write_word_data(self.__addr, self.CH1_DUTY_MAX, val)
            i2c.write_word_data(self.__addr, self.CH2_DUTY_MAX, val)
            self.__req |= self.REQ_CH1_DUTY_MAX | self.REQ_CH2_DUTY_MAX
            if self.Get_servo_state("1") == 1 or self.Get_servo_state("2") == 1:
                print("Please turn off ALL CH POWER.")
        else:
            print("invalid command")

    def Set_servo_duty_min(self, ch, val_str):
        val = struct.unpack(">H", struct.pack("<H", int(val_str)))[0]
        if ch == "1":
            i2c.write_word_data(self.__addr, self.CH1_DUTY_MIN, val)
            self.__req |= self.REQ_CH1_DUTY_MIN
            if self.Get_servo_state(ch) == 1:
                print("Please turn off CH1 POWER.")
        elif ch == "2":
            i2c.write_word_data(self.__addr, self.CH2_DUTY_MIN, val)
            self.__req |= self.REQ_CH2_DUTY_MIN
            if self.Get_servo_state(ch) == 1:
                print("Please turn off CH2 POWER.")
        elif ch == "b":
            i2c.write_word_data(self.__addr, self.CH1_DUTY_MIN, val)
            i2c.write_word_data(self.__addr, self.CH2_DUTY_MIN, val)
            self.__req |= self.REQ_CH1_DUTY_MIN | self.REQ_CH2_DUTY_MIN
            if self.Get_servo_state("1") == 1 or self.Get_servo_state("2") == 1:
                print("Please turn off ALL CH POWER.")
        else:
            print("invalid command")

    def Set_servo_cycle(self, val_str):
        val = struct.unpack(">H", struct.pack("<H", int(val_str)))[0]
        i2c.write_word_data(self.__addr, self.PWM_CYCL, val)
        self.__req |= self.REQ_PWM_CYCL
        if self.Get_servo_state("1") == 1 or self.Get_servo_state("2") == 1:
            print("Please turn off ALL CH POWER.")

    # -------------------------------------------------------------------------------------------------------------------------------------

    def Set_servo_Write(self):
        print(repr(self.__req))
        i2c.write_byte_data(self.__addr, self.REQ_SET_VAL, self.__req)
        self.__req = 0x0

    def __init__(self):
        self.Servo_Switch("b", self.OFF)

        self.Set_servo_duty_max("b", self.INIT_SVO_MAX)
        self.Set_servo_duty_min("b", self.INIT_SVO_MIN)

        self.Set_servo_cycle(self.INIT_SVO_CCL)

        self.Set_servo_duty("1", self.INIT_SVO_MAX)
        self.Set_servo_duty("2", self.INIT_SVO_MIN)

        self.Set_servo_Write()

        self.Servo_Switch("b", self.ON)

#!/usr/bin/python3

import smbus
import math
import json

POWER_MANAGEMENT_1 = 0x6b
POWER_MANAGEMENT_2 = 0x6c

GYRO_X = 0x43
GYRO_Y = 0x45
GYRO_Z = 0x47
GYRO_SCALE = 131

ACCELLERATION_X = 0x3b
ACCELLERATION_Y = 0x3d
ACCELLERATION_Z = 0X3f
ACCELLERATION_SCALE = 16384.0


def read_byte(reg):
    return bus.read_byte_data(address, reg)


def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, POWER_MANAGEMENT_1, 0)

while True:
    accelleration_x = read_word_2c(ACCELLERATION_X)
    accelleration_y = read_word_2c(ACCELLERATION_Y)
    accelleration_z = read_word_2c(ACCELLERATION_Z)
    accelleration_x_scaled = accelleration_x / ACCELLERATION_SCALE
    accelleration_y_scaled = accelleration_y / ACCELLERATION_SCALE
    accelleration_z_scaled = accelleration_z / ACCELLERATION_SCALE

    sample = {
        'gyro': {
            'x': read_word_2c(GYRO_X),
            'y': read_word_2c(GYRO_Y),
            'z': read_word_2c(GYRO_Z),
        },
        'accelleration': {
            'x': accelleration_x,
            'y': accelleration_y,
            'z': accelleration_z,
            'x_scaled': accelleration_x_scaled,
            'y_scaled': accelleration_y_scaled,
            'z_scaled': accelleration_z_scaled,
        },
        'rotation': {
            'x': get_x_rotation(accelleration_x_scaled, accelleration_y_scaled, accelleration_z_scaled),
            'y': get_y_rotation(accelleration_x_scaled, accelleration_y_scaled, accelleration_z_scaled),
        },
    }

    print(json.dumps(sample, indent=4))

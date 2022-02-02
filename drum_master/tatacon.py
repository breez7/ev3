#!/usr/bin/env python3

print("loading ..")

from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
import evdev, time
from evdev import InputDevice, categorize, ecodes
from ev3dev2.sound import Sound

unk = -1
NULL_CHAR = chr(0)
hid_keyboard = [
    0,  0,  0,  0, 30, 48, 46, 32, 18, 33, 34, 35, 23, 36, 37, 38,
    50, 49, 24, 25, 16, 19, 31, 20, 22, 47, 17, 45, 21, 44,  2,  3,
    4,  5,  6,  7,  8,  9, 10, 11, 28,  1, 14, 15, 57, 12, 13, 26,
    27, 43, 43, 39, 40, 41, 51, 52, 53, 29, 113, 114, 115, 165, 164, 163,
    158, 172, 127, 68, 87, 88, 99, 70,119,110,102,104,111,107,109,106,
    105,108,103, 69, 98, 55, 74, 78, 96, 79, 80, 81, 75, 76, 77, 71,
    72, 73, 82, 83, 86,67,116,117,183,184,185,186,187,188,189,190,
    191,192,193,194,134,138,130,132,128,129,131,137,133,135,136,59,
    61,60,unk,unk,unk,121,unk, 89, 93,124, 92, 94, 95,unk,unk,unk,
    122,123, 90, 91, 85,unk,unk,unk,unk,unk,unk,unk,111,unk,unk,unk,
    unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,
    unk,unk,unk,unk,unk,unk,179,180,unk,unk,unk,unk,unk,unk,unk,unk,
    unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,unk,
    unk,unk,unk,unk,unk,unk,unk,unk,111,unk,unk,unk,unk,unk,unk,unk,
    58, 42, 56,125, 97, 54,100,126,63,166,62,64,161,115,114,113,
    150,65,159,128,136,177,178,176,142,152,173,140,unk,unk,unk,unk
    ]
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(bytes(report, encoding='utf8'))

ts1 = TouchSensor(INPUT_1)
ts2 = TouchSensor(INPUT_2)
ts3 = TouchSensor(INPUT_3)
ts4 = TouchSensor(INPUT_4)

print("started ..")
new_ts1 = True
new_ts2 = True
new_ts3 = True
new_ts4 = True

sound = Sound()
sound.speak('I am ready')

while True:
    if ts1.is_pressed and new_ts1:
        write_report(NULL_CHAR*2 + chr(hid_keyboard.index(evdev.ecodes.KEY_F)) + NULL_CHAR*5)
        new_ts1 = False
    if ts1.is_released:
        write_report(NULL_CHAR*8)
        new_ts1 = True
    if ts2.is_pressed and new_ts2:
        write_report(NULL_CHAR*2 + chr(hid_keyboard.index(evdev.ecodes.KEY_J)) + NULL_CHAR*5)
        new_ts2 = False
    if ts2.is_released:
        write_report(NULL_CHAR*8)
        new_ts2 = True
    if ts3.is_pressed and new_ts3:
        write_report(NULL_CHAR*2 + chr(hid_keyboard.index(evdev.ecodes.KEY_D)) + NULL_CHAR*5)
        new_ts3 = False
    if ts3.is_released:
        write_report(NULL_CHAR*8)
        new_ts3 = True
    if ts4.is_pressed and new_ts4:
        write_report(NULL_CHAR*2 + chr(hid_keyboard.index(evdev.ecodes.KEY_K)) + NULL_CHAR*5)
        new_ts4 = False
    if ts4.is_released:
        write_report(NULL_CHAR*8)
        new_ts4 = True

    # sleep(0.005)
    sleep(0.01)


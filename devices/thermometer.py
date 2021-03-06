import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

DEVICES_DIR = '/sys/bus/w1/devices/'


def get_temperature():
    return {
        'top': 25.6,
        'bottom': 28.9
    }

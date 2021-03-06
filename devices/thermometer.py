import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

DEVICES_DIR = '/sys/bus/w1/devices/'
t1 = '28-3c01d07524fa'
t2 = '28-3c01d075439b'


def get_temperature():
    return {
        'top': 25.6,
        'bottom': 28.9
    }

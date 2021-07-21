import os
import time

from logger import LOGGER

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

DEVICE_PATH = '/sys/bus/w1/devices/{device_id}/w1_slave'
DEVICE_ID_TOP = '28-00000d402c2c'
DEVICE_ID_BOTTOM = '28-00000d4044c5'
DEVICE_ID_EXTERNAL = '28-3c01d6071af0'


class Thermometer:
    def __init__(self, device_id):
        self.device_id = device_id

    def get_temperature(self):
        device_file = DEVICE_PATH.format(device_id=self.device_id)
        lines = None
        empty_reads = 0
        while not lines or len(lines) == 0 or lines[0].strip()[-3:] != 'YES':
            try:
                with open(device_file, 'r') as f:
                    lines = f.readlines()
            except FileNotFoundError:
                LOGGER.warn(f'file {device_file} not found')
                time.sleep(1)
            if not lines or len(lines) == 0:
                empty_reads += 1
                if empty_reads%100 == 0:
                    LOGGER.error(f'file {device_file} is empty too long')
                    return None
                time.sleep(0.2)

        temp_pos = lines[1].find('t=')
        if temp_pos != -1:
            temp_string = lines[1][temp_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return round(temp_c, 2)
        else:
            LOGGER.error(f"Can't read temperature for {self.device_id}")
            return None

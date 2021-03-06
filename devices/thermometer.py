import os
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

DEVICE_PATH = '/sys/bus/w1/devices/{device_id}/w1_slave'
DEVICE_ID_TOP = '28-3c01d075439b'
DEVICE_ID_BOTTOM = '28-3c01d07524fa'


def read_temp_raw(device_id):
    device_file = DEVICE_PATH.format(device_id=device_id)
    lines = None
    # TODO: логирование/оповещение, что термометр пропал
    while not lines or len(lines) == 0 or lines[0].strip()[-3:] != 'YES':
        with open(device_file, 'r') as f:
            lines = f.readlines()
        if not lines:
            time.sleep(0.2)

    temp_pos = lines[1].find('t=')
    if temp_pos != -1:
        temp_string = lines[1][temp_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return round(temp_c, 2)
    else:
        raise ValueError(f"Can't read temperature for {device_id}")


def get_temperature():
    return {
        'top': read_temp_raw(DEVICE_ID_TOP),
        'bottom': read_temp_raw(DEVICE_ID_BOTTOM)
    }

import os
import glob
import time

os.system("modprobe w1-gpio")
os.system("modprobe w1-therm")

base_dir = '/sys/bus/w1/devices/'
device_folders = glob.glob(base_dir + '28*')
while (len(device_folders) != 2):
    device_folders = glob.glob(base_dir + '28*')
    print('read again')


def read_temp_raw(id):
    device_file = device_folders[id] + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(id):
    lines = read_temp_raw(id)
    while len(lines) == 0 or lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(id)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


while True:
    print('Bottom: ' + str(round(read_temp(0), 1)) + ' °C')
    print('Top: ' + str(round(read_temp(1), 1)) + ' °C')
    print('------------------')
    time.sleep(5)

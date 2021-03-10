import os
import time

from logger import get_logger

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

DEVICE_PATH = '/sys/bus/w1/devices/{device_id}/w1_slave'
DEVICE_ID_TOP = '28-3c01d075439b'
DEVICE_ID_BOTTOM = '28-3c01d07524fa'
DEVICE_ID_MAP = {
    'top': DEVICE_ID_TOP,
    'bottom': DEVICE_ID_BOTTOM
}
MAX_TEMPERATURE = 26
NORMAL_TEMPERATURE = 24
LOGGER = get_logger()


class TempController:
    def __init__(self, name, fan, state):
        self.pwm_speed = 0
        self.name = name
        self.fan = fan
        self.state = state

    def temp_control(self):
        temp_new = self.get_temperature()
        self.update_pwm(temp_new)

    def update_pwm(self, temp_new):
        if temp_new >= MAX_TEMPERATURE:
            self.pwm_speed = 100
        elif temp_new <= NORMAL_TEMPERATURE:
            self.pwm_speed = 0
        elif temp_new > NORMAL_TEMPERATURE:
            self.pwm_speed = self.pwm_speed + 5
        self.fan.set_speed(self.pwm_speed)
        self.state['fan'][self.name] = self.pwm_speed
        self.state['thermometer'][self.name] = temp_new
        LOGGER.info(self.state)

    def get_temperature(self):
        device_id = DEVICE_ID_MAP[self.name]
        device_file = DEVICE_PATH.format(device_id=device_id)
        lines = None
        # TODO: логирование/оповещение, что термометр пропал
        while not lines or len(lines) == 0 or lines[0].strip()[-3:] != 'YES':
            try:
                with open(device_file, 'r') as f:
                    lines = f.readlines()
            except FileNotFoundError:
                LOGGER.warn(f'file {device_file} not found')
                time.sleep(3)
            if not lines:
                time.sleep(0.2)

        temp_pos = lines[1].find('t=')
        if temp_pos != -1:
            temp_string = lines[1][temp_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return round(temp_c, 2)
        else:
            raise ValueError(f"Can't read temperature for {device_id}")

from devices.fan import Fan, FAN_TOP_PIN, FAN_BOTTOM_PIN, MAX_SPEED
from devices.thermometer import Thermometer, DEVICE_ID_TOP, DEVICE_ID_BOTTOM

BOTH_LIGHT_TEMPERATURE_THRESHOLD = 31
NORMAL_TEMPERATURE_MAX = 28
NORMAL_TEMPERATURE = 24


class TemperatureController:
    def __init__(self, state):
        self.fan_top = Fan(FAN_TOP_PIN, 10)
        self.fan_bottom = Fan(FAN_BOTTOM_PIN, 0)
        self.thermometer_top = Thermometer(DEVICE_ID_TOP)
        self.thermometer_bottom = Thermometer(DEVICE_ID_BOTTOM)
        self.state = state

    def update_fan_pwm(self):
        self._update_fan_pwm(self.fan_top, self.thermometer_top, 'top')
        self._update_fan_pwm(self.fan_bottom, self.thermometer_bottom, 'bottom')

    def _update_fan_pwm(self, fan, thermometer, name):
        temperature = thermometer.get_temperature()
        if not temperature:
            return
        if temperature >= NORMAL_TEMPERATURE_MAX:
            speed = MAX_SPEED
        elif temperature <= NORMAL_TEMPERATURE:
            speed = fan.min_speed
        elif temperature > NORMAL_TEMPERATURE and self.state['fan'][name] <= MAX_SPEED - 5:
            speed = self.state['fan'][name] + 5
        else:
            speed = MAX_SPEED

        fan.set_speed(speed)
        self.state['fan'][name] = speed
        self.state['thermometer'][name] = temperature

    def stop(self):
        self.fan_top.stop()
        self.fan_bottom.stop()

import schedule
import time
import RPi.GPIO as GPIO

from controllers.light_controller import LightController
from controllers.sensors_data_collector import SensorsDataCollector
from controllers.temperature_controller import TemperatureController
from devices.fan import MAX_SPEED
from logger import LOGGER


STATE = {
    'fan': {
        'top': MAX_SPEED,
        'bottom': MAX_SPEED
    },
    'thermometer': {
        'top': None,
        'bottom': None,
        'external': None
    },
    'light': {
        '1': 'OFF',
        '2': 'OFF'
    }
}


def main():
    try:
        def log_state():
            LOGGER.info(STATE)

        temperature_controller = TemperatureController(STATE)
        sensors_data_collector = SensorsDataCollector(STATE)
        light_controller = LightController(STATE)

        schedule.every(10).seconds.do(temperature_controller.update_fan_pwm)
        schedule.every(10).seconds.do(sensors_data_collector.get_data)
        schedule.every(10).seconds.do(light_controller.control)
        schedule.every(10).seconds.do(log_state)

        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        temperature_controller.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    main()

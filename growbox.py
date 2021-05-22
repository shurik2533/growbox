import schedule
import time
import RPi.GPIO as GPIO

from controllers.sensors_data_collector import SensorsDataCollector
from controllers.temperature_controller import TemperatureController
from devices.fan import MAX_SPEED
from logger import get_logger

GPIO.setmode(GPIO.BCM)

LOGGER = get_logger()

STATE = {
    'fan': {
        'top': MAX_SPEED,
        'bottom': MAX_SPEED
    },
    'thermometer': {
        'top': None,
        'bottom': None,
        'external': None
    }
}


def main():
    try:
        def log_state():
            LOGGER.info(STATE)

        temperature_controller = TemperatureController(STATE)
        sensors_data_collector = SensorsDataCollector(STATE)

        schedule.every(10).seconds.do(temperature_controller.update_fan_pwm)
        schedule.every(10).seconds.do(sensors_data_collector.get_data)
        schedule.every(10).seconds.do(log_state)

        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()

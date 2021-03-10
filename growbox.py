import schedule
import time
import RPi.GPIO as GPIO
from devices.fan import Fan
from devices.thermometer import TempController

GPIO.setmode(GPIO.BCM)

STATE = {
    'fan': {
        'top': None,
        'bottom': None
    },
    'thermometer': {
        'top': None,
        'bottom': None
    }
}


def main():
    try:
        fan_top = Fan(17)
        fan_bottom = Fan(27)

        temp_top = TempController('top', fan_top, STATE)
        temp_bottom = TempController('bottom', fan_bottom, STATE)

        schedule.every(10).seconds.do(temp_top.temp_control)
        schedule.every(10).seconds.do(temp_bottom.temp_control)

        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        fan_top.stop()
        fan_bottom.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    main()

import queue
import threading

import schedule
import time
import RPi.GPIO as GPIO

from controllers.heat_controller import HeatController
from controllers.light_controller import LightController
from controllers.sensors_data_collector import SensorsDataCollector
from controllers.temperature_controller import TemperatureController
from controllers.watering_controller import WateringController
from logger import LOGGER
from state import STATE


def main():
    def worker_main():
        while True:
            job_func = jobqueue.get()
            job_func()
            jobqueue.task_done()

    jobqueue = queue.Queue()

    try:
        def log_state():
            LOGGER.info(STATE)

        temperature_controller = TemperatureController(STATE)
        sensors_data_collector = SensorsDataCollector(STATE)
        light_controller = LightController(STATE)
        watering_controller_top = WateringController(STATE, 'top')
        watering_controller_bottom = WateringController(STATE, 'bottom')
        heat_controller = HeatController(STATE)

        schedule.every(10).seconds.do(jobqueue.put, temperature_controller.update_fan_pwm)
        schedule.every(10).seconds.do(jobqueue.put, sensors_data_collector.get_data)
        schedule.every(60).seconds.do(jobqueue.put, light_controller.control)
        schedule.every(10).seconds.do(jobqueue.put, watering_controller_top.control)
        schedule.every(10).seconds.do(jobqueue.put, watering_controller_bottom.control)
        schedule.every(10).seconds.do(jobqueue.put, heat_controller.control)
        schedule.every(10).seconds.do(jobqueue.put, log_state)

        worker_thread = threading.Thread(target=worker_main)
        worker_thread.start()

        while True:
            schedule.run_pending()
            time.sleep(1)
    finally:
        temperature_controller.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    main()

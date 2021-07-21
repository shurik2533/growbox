import datetime
import json
import queue
import threading

import joblib
import schedule
import time
import RPi.GPIO as GPIO

from controllers.heat_controller import HeatController
from controllers.light_controller import LightController
from controllers.sensors_data_collector import SensorsDataCollector
from controllers.temperature_controller import TemperatureController
from controllers.watering_controller import WateringController
from db.log import save_state_to_db
from logger import LOGGER
from state import STATE, STATE_PATH


def main():
    def worker_main():
        while True:
            job_func = jobqueue.get()
            try:
                job_func()
            except:
                LOGGER.exception('')
            jobqueue.task_done()

    jobqueue = queue.Queue()

    try:
        def log_state():
            def default(o):
                if isinstance(o, (datetime.date, datetime.datetime)):
                    return o.isoformat()
            state_string = json.dumps(STATE, default=default)
            LOGGER.info(state_string)
            save_state_to_db(state_string)
            joblib.dump(STATE, STATE_PATH)

        def log_job_queue_size():
            job_queue_len = len(jobqueue)
            LOGGER.log(f'job_queue_len: {job_queue_len}')

        temperature_controller = TemperatureController(STATE)
        sensors_data_collector = SensorsDataCollector(STATE)
        light_controller = LightController(STATE)
        watering_controller_top = WateringController(STATE, 'top')
        watering_controller_bottom = WateringController(STATE, 'bottom')
        heat_controller = HeatController(STATE)

        schedule.every(10).seconds.do(jobqueue.put, temperature_controller.update_fan_pwm)
        schedule.every(10).seconds.do(jobqueue.put, sensors_data_collector.get_data)
        schedule.every(300).seconds.do(jobqueue.put, light_controller.control)
        schedule.every().day.at("10:30").do(jobqueue.put, watering_controller_top.control)
        schedule.every().day.at("10:30").do(jobqueue.put, watering_controller_bottom.control)
        # schedule.every().day.at("20:30").do(jobqueue.put, watering_controller_top.control)
        # schedule.every().day.at("20:30").do(jobqueue.put, watering_controller_bottom.control)
        schedule.every(120).seconds.do(jobqueue.put, heat_controller.control)
        schedule.every(10).seconds.do(jobqueue.put, log_state)
        schedule.every(10).seconds.do(jobqueue.put, log_job_queue_size)

        worker_thread = threading.Thread(target=worker_main)
        worker_thread.start()

        while True:
            schedule.run_pending()
            time.sleep(1)
    except:
        LOGGER.exception('')
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()

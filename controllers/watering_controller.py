import time
from datetime import datetime, timedelta
from devices import relay
from devices.relay import PUMP_TOP, PUMP_BOTTOM

TOP_THRESHOLD = 20000
BOTTOM_THRESHOLD = 20000
WATERING_TIME = 20  # sec
MIN_TIME_FOR_THE_NEXT_WATERING = 3  # min


class WateringController:
    def __init__(self, state, location):
        self.state = state
        if location == 'top':
            self.threshold = TOP_THRESHOLD
            self.pin = PUMP_TOP
        else:
            self.threshold = BOTTOM_THRESHOLD
            self.pin = PUMP_BOTTOM

        self.location = location

    def control(self):
        value = self.state['soil_moisture'][self.location]
        last_watering_time = self.state['last_watering_time'][self.location]
        min_next_watering = last_watering_time + timedelta(minutes=MIN_TIME_FOR_THE_NEXT_WATERING)

        if value > self.threshold and datetime.now() > min_next_watering:
            try:
                relay.on(self.pin)
                self.state['last_watering_time'][self.location] = datetime.now()
                time.sleep(WATERING_TIME)
            finally:
                relay.off(self.pin)

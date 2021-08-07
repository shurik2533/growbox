import time
from datetime import datetime
from devices import relay
from devices.relay import PUMP_TOP, PUMP_BOTTOM

WATERING_TIME_TOP = 90  # sec
WATERING_TIME_BOTTOM = 80  # sec


class WateringController:
    def __init__(self, state, location):
        self.state = state
        if location == 'top':
            self.pin = PUMP_TOP
            self.watering_time = WATERING_TIME_TOP
        else:
            self.pin = PUMP_BOTTOM
            self.watering_time = WATERING_TIME_BOTTOM

        self.location = location

    def control(self):
        try:
            relay.on(self.pin)
            self.state['last_watering_time'][self.location] = datetime.now()
            time.sleep(self.watering_time)
        finally:
            relay.off(self.pin)

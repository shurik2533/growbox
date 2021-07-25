import time
from datetime import datetime
from devices import relay
from devices.relay import PUMP_TOP, PUMP_BOTTOM

WATERING_TIME = 40  # sec


class WateringController:
    def __init__(self, state, location):
        self.state = state
        if location == 'top':
            self.pin = PUMP_TOP
        else:
            self.pin = PUMP_BOTTOM

        self.location = location

    def control(self):
        try:
            relay.on(self.pin)
            self.state['last_watering_time'][self.location] = datetime.now()
            time.sleep(WATERING_TIME)
        finally:
            relay.off(self.pin)

import time
from datetime import datetime, timedelta
from devices import relay
from devices.relay import PUMP_TOP, PUMP_BOTTOM

MIN_TEMPERATURE = 10
HEAT_PIN = 7


class HeatController:
    def __init__(self, state):
        self.state = state

    def control(self):
        if min(self.state['thermometer']['top'], self.state['thermometer']['bottom']) < MIN_TEMPERATURE:
            relay.on(HEAT_PIN)
            self.state['heat'] = 'ON'
        else:
            relay.off(HEAT_PIN)
            self.state['heat'] = 'OFF'

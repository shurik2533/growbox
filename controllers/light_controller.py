from datetime import datetime

from config.config import MODE
from controllers.temperature_controller import BOTH_LIGHT_TEMPERATURE_THRESHOLD
from devices import relay
from devices.relay import LIGHT_1, LIGHT_2

DAY_STARTS_AT = '07:00'
DAY_ENDS_AT = '20:00'
LIGHT_MODE = 'both'  # one/both



class LightController:
    def __init__(self, state):
        self.state = state

    def control(self):
        if self._is_light_on():
            if LIGHT_MODE == 'both':
                relay.on(LIGHT_1)
                self.state['light']['1'] = 'ON'
                relay.on(LIGHT_2)
                self.state['light']['2'] = 'ON'
            else:
                relay.on(LIGHT_1)
                self.state['light']['1'] = 'ON'
                relay.off(LIGHT_2)
                self.state['light']['2'] = 'OFF'
        else:
            relay.off(LIGHT_1)
            self.state['light']['1'] = 'OFF'
            relay.off(LIGHT_2)
            self.state['light']['2'] = 'OFF'

    def _is_light_on(self):
        if MODE['light'] == 'OFF':
            return False
        if max(self.state['thermometer']['top'], self.state['thermometer']['bottom']) > BOTH_LIGHT_TEMPERATURE_THRESHOLD:
            return False

        now = datetime.now()
        minutes_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/60

        def get_minutes(s):
            arr = [int(v) for v in s.split(':')]
            return arr[0] * 60 + arr[1]
        minutes_start = get_minutes(DAY_STARTS_AT)
        minutes_end = get_minutes(DAY_ENDS_AT)
        if minutes_start > minutes_end:
            return (0 <= minutes_since_midnight <= minutes_end) or (minutes_start <= minutes_since_midnight <= 24*60)
        else:
            return minutes_start <= minutes_since_midnight <= minutes_end

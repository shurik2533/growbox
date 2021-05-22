from devices import relay
from devices.relay import LIGHT_1, LIGHT_2


class LightController:
    def __init__(self, state):
        self.state = state

    def control(self):
        if self.state['light']['1'] == 'OFF':
            relay.on(LIGHT_1)
            self.state['light']['1'] = 'ON'

        if self.state['light']['2'] == 'OFF':
            relay.on(LIGHT_2)
            self.state['light']['2'] = 'ON'

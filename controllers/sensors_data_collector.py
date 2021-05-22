from devices.thermometer import Thermometer, DEVICE_ID_EXTERNAL


class SensorsDataCollector:
    def __init__(self, state):
        self.state = state
        self.thermometer_external = Thermometer(DEVICE_ID_EXTERNAL)

    def get_data(self):
        self.state['thermometer']['external'] = self.thermometer_external.get_temperature()

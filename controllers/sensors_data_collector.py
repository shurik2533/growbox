from devices.co2 import Co2
from devices.humidity import Humidity
from devices.soil_moisture import SoilMoisture
from devices.thermometer import Thermometer, DEVICE_ID_EXTERNAL


class SensorsDataCollector:
    def __init__(self, state):
        self.state = state
        self.thermometer_external = Thermometer(DEVICE_ID_EXTERNAL)
        self.humidity_sensor = Humidity()
        self.co2_sensor = Co2()
        self.soil_moisture = SoilMoisture()

    def get_data(self):
        self.state['thermometer']['external'] = self.thermometer_external.get_temperature()

        humidity_sensor_data = self.humidity_sensor.get_data()
        self.state['humidity']['humidity'] = humidity_sensor_data['humidity']
        self.state['humidity']['temperature'] = humidity_sensor_data['temperature']

        co2_sensor_data = self.co2_sensor.get_data()
        self.state['co2']['co2'] = co2_sensor_data['co2']
        self.state['co2']['temperature'] = co2_sensor_data['temperature']

        soil_moisture_data = self.soil_moisture.get_data()
        self.state['soil_moisture']['top'] = soil_moisture_data[0]
        self.state['soil_moisture']['bottom'] = soil_moisture_data[1]

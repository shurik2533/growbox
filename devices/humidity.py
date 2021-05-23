import board
import adafruit_si7021


class Humidity:
    def __init__(self):
        self.sensor = adafruit_si7021.SI7021(board.I2C())

    def get_data(self):
        return {
            'temperature': round(self.sensor.temperature, 2),
            'humidity': round(self.sensor.relative_humidity, 2)
        }

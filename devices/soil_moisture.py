import Adafruit_ADS1x15

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1


class SoilMoisture:
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.channels = 4

    def get_data(self):
        # Read all the ADC channel values in a list.
        values = [0] * self.channels
        for i in range(self.channels):
            # Read the specified ADC channel using the previously set gain value.
            values[i] = self.adc.read_adc(i, gain=GAIN, data_rate=128)
        return values[0:2]

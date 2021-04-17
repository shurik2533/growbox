import time
import board
import busio
import adafruit_ccs811
import adafruit_si7021
 
i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c)
sensor = adafruit_si7021.SI7021(board.I2C())
 
# Wait for the sensor to be ready
while not ccs811.data_ready:
    pass
 
i = 0
temp = 0
hum = 0
while True:
    try:
        if i%30 == 0:
            temp = round(sensor.temperature, 1)
            hum = int(sensor.relative_humidity)
            ccs811.set_environmental_data(hum, temp)
        print("CO2: {} PPM, TVOC: {} PPB, Temperature: {} C, Humidity: {} %".format(ccs811.eco2, ccs811.tvoc, temp, hum))
        i = i + 1
    except:
        print("error")
    time.sleep(1)

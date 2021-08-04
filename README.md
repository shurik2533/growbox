# Growbox
Code for my smart growbox experiment.

Growbox control based on Raspberry Pi. Supported devices/sensors:
- Themperature sensors: DS18B20
- 16-Bit ADC: ADS1115
- Multiple channel relay
- Humidity and Temperature Sensor: Si7021-A20
- PWM fans control
- CO2 and Temperature Sensor: MH-Z19

# Running
Works only with sudo because of CO2 sensor use `/dev/serial0` which requires root permission

`sudo python3 growbox.py` 

# Run as a service
`sudo apt-get install supervisor`

Create a config file for your daemon at `/etc/supervisor/conf.d/growbox.conf`

```
[program:growbox]
[program:growbox]
directory=/home/pi/growbox
command=sudo python3 growbox.py
autostart=true
autorestart=true
stderr_logfile=/home/pi/growbox/logs/supervisor.err.log
stdout_logfile=/home/pi/growbox/logs/supervisor.out.log
stdout_logfile_maxbytes=0
```

Restart supervisor to load your growbox.conf`
```
sudo supervisorctl update
sudo supervisorctl restart growbox
```

# growbox
Code for my smart growbox experiment

Works only with sudo because of CO2 sensor use `/dev/serial0` which requires root permission

`sudo python3 growbox.py` 

# run as a service
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

Restart supervisor to load your new .conf
```
sudo supervisorctl update
sudo supervisorctl restart growbox
```

# Don't try to run this as a script or it will all be over very quickly  
# it won't do any harm though.  
# these are all the elements you need to control PWM on 'normal' GPIO ports  
# with RPi.GPIO - requires RPi.GPIO 0.5.2a or higher  

import RPi.GPIO as GPIO # always needed with RPi.GPIO  

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  

GPIO.setup(25, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port  

p = GPIO.PWM(25, 50)    # create an object p for PWM on port 25 at 50 Hertz  
# you can have more than one of these, but they need
# different names for each port
# e.g. p1, p2, motor, servo1 etc.

p.start(50)             # start the PWM on 50 percent duty cycle  
# duty cycle value can be 0.0 to 100.0%, floats are OK

p.ChangeDutyCycle(90)   # change the duty cycle to 90%  

p.ChangeFrequency(100)  # change the frequency to 100 Hz (floats also work)  
# e.g. 100.5, 5.2

p.stop()                # stop the PWM output  

GPIO.cleanup()          # when your program exits, tidy up after yourself

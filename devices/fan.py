# Don't try to run this as a script or it will all be over very quickly  
# it won't do any harm though.  
# these are all the elements you need to control PWM on 'normal' GPIO ports  
# with RPi.GPIO - requires RPi.GPIO 0.5.2a or higher  

import RPi.GPIO as GPIO # always needed with RPi.GPIO  
import time

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  

GPIO.setup(17, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port
GPIO.setup(27, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port

p1 = GPIO.PWM(17, 1000)    # create an object p for PWM on port 25 at 50 Hertz
p2 = GPIO.PWM(27, 1000)    # create an object p for PWM on port 25 at 50 Hertz
# you can have more than one of these, but they need
# different names for each port
# e.g. p1, p2, motor, servo1 etc.
print(100)
p1.start(100)             # start the PWM on 50 percent duty cycle
p2.start(100)             # start the PWM on 50 percent duty cycle
# duty cycle value can be 0.0 to 100.0%, floats are OK

#p1.ChangeDutyCycle(10)   # change the duty cycle to 90%

# e.g. 100.5, 5.2

time.sleep(5)

#
print(90)
p1.ChangeDutyCycle(90)
p2.ChangeDutyCycle(90)
time.sleep(5)


print(80)
p1.ChangeDutyCycle(80)
p2.ChangeDutyCycle(80)
time.sleep(5)


print(70)
p1.ChangeDutyCycle(70)
p2.ChangeDutyCycle(70)
time.sleep(5)


print(60)
p1.ChangeDutyCycle(60)
p2.ChangeDutyCycle(60)
time.sleep(5)


print(50)
p1.ChangeDutyCycle(50)
p2.ChangeDutyCycle(50)
time.sleep(5)


print(40)
p1.ChangeDutyCycle(40)
p2.ChangeDutyCycle(40)
time.sleep(5)


print(30)
p1.ChangeDutyCycle(30)
p2.ChangeDutyCycle(30)
time.sleep(5)

print(20)
p1.ChangeDutyCycle(20)
p2.ChangeDutyCycle(20)
time.sleep(5) 

print(10)
p1.ChangeDutyCycle(10)
p2.ChangeDutyCycle(10)
time.sleep(5) 

print(5)
p1.ChangeDutyCycle(5)
p2.ChangeDutyCycle(5)
time.sleep(5) 

print(0)
p1.ChangeDutyCycle(0)
p2.ChangeDutyCycle(0)
time.sleep(5) 

# p2.ChangeDutyCycle(100)
#
# time.sleep(5)


p1.stop()
p2.stop()        # stop the PWM output

GPIO.cleanup()          # when your program exits, tidy up after yourself

from RPIO import PWM

servo = PWM.Servo()

# Set servo on GPIO17 to 1200µs (1.2ms)
servo.set_servo(17, 1200)

# Clear servo on GPIO17
servo.stop_servo(17)

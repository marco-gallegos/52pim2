import RPi.GPIO as GPIO
import time
import subprocess as sp


# initializing gpio, settings mode to board
# default pin on fan is physical pin 8, GPIO14
Fan:int = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Fan, GPIO.OUT)

p = GPIO.PWM(Fan, 50)
p.start(0)

try:
    pass
    while True:
        temp = sp.getoutput("vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'")
        print(temp)
        if float(temp) < 48.0:
            p.ChangeDutyCycle(100)
            time.sleep(1)
        elif float(temp) >= 48.0:
            print("max speed")
            p.ChangeDutyCycle(100)
            time.sleep(5)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

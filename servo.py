import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

def setservo(deg): #-90<=deg<=90
    deg+=90.0
    sec=(0.5+1.9*(deg/180.0))/20.0*100.0
    servo.ChangeDutyCycle(sec)

for i in range(1):
	servo.ChangeDutyCycle(bottom)
	time.sleep(1.0)

	servo.ChangeDutyCycle(middle)
	time.sleep(1.0)

	servo.ChangeDutyCycle(top)
	time.sleep(1.0)

        setservo(-90.0)
        time.sleep(1.0)

        setservo(0.0)
        time.sleep(1.0)

        setservo(90.0)
        time.sleep(1.0)





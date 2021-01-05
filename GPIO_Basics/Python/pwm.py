import RPi.GPIO as GPIO
import time

ledPin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, 500) #500 Hz
    p.start(0) #starts PWM with a duty cycle of 0.

def loop():
    while True:
        for dc in range(0,101):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    p.stop() #stop PWM
    GPIO.cleanup()

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
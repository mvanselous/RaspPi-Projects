import RPi.GPIO as GPIO
import time

#This component has distinct + and - sides.
#The inputs are along the side with the label.

ledPins = [11,12,13,15,16,18,22,3,5,24]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.output(ledPins,GPIO.HIGH)
    
def loop():
    while True:
        for pin in ledPins:
            print(f'{pin} off')
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[::-1]:
            print(pin)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.HIGH)
            
def destroy():
    GPIO.cleanup()

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
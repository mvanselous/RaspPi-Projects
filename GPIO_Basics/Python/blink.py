import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setmode(GPIO.BCM)
    #if we used GPIO.BCM, then the numbering would match the board extender
    #So pin 11 -> 17
    
    #Use the command "pinout" in the linux terminal to see the complete mapping.
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('using pin%d'%ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('led on >>>')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print('led off <<<')
        time.sleep(1)
    
def destroy():
    GPIO.cleanup()

setup()

try:
    loop()
except KeyboardInterrupt:
    destroy()
        
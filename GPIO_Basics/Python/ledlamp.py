import RPi.GPIO as GPIO
import time

ledPin = 11
buttonPin = 12
ledState = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonEvent(channel):
    global ledState
    print('buttonEvent GPIO%d' %channel)
    ledState = not ledState
    if ledState:
        print('led on')
    else:
        print('led off')
    GPIO.output(ledPin,ledState)

def loop():
    GPIO.add_event_detect(buttonPin,GPIO.FALLING,callback=buttonEvent,bouncetime=300)
    while True:
        pass

def destroy():
    GPIO.cleanup()

setup()
try:
    loop()
except KeyboardInterrupt:
    destroy()
    
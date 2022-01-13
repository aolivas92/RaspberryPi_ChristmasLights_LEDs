import RPi.GPIO as GPIO
import time

Red = 17
Green = 23

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Red, GPIO.OUT)
    GPIO.setup(Green, GPIO.OUT)
    GPIO.output(Red, GPIO.LOW)
    GPIO.output(Green, GPIO.LOW)
    print('pin ' + str(Red) + ' and pin ' + str(Green) + ' are ready')

def end():
    print('goodbye')
    GPIO.cleanup()

def light_mode(res):
    if res == 'seperate':
        while True:
            GPIO.output(Red, GPIO.HIGH)
            GPIO.output(Green, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(Red, GPIO.LOW)
            GPIO.output(Green, GPIO.HIGH)
            time.sleep(0.2)
    elif res == 'together':
        while True:
            GPIO.output(Red, GPIO.HIGH)
            GPIO.output(Green, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(Red, GPIO.LOW)
            GPIO.output(Green, GPIO.LOW)
            time.sleep(0.2)

def lights_On(res):
    if res == 'yes':
        res = input('Do you want them to flash seperate or together \n>')
        if (res == 'seperate') or (res == 'together'):
           light_mode(res)
        else:
            print('Try again')
            lights_On('yes')
    elif res == 'no':
        end()
    else:
        print('Try again')
        res = input('Do you want the lights on? \n>')
        lights_On(res)

setup()
res = input('Do you want the lights on? \n>')
try:
    lights_On(res)
except KeyboardInterrupt:
    end()
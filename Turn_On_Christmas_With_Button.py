from gpiozero import LED, Button
from signal import pause
import time

print('Program is starting...')

current_state = False
Red = LED('GPIO17')
Green = LED('GPIO23')
button = Button('GPIO18')

def Button_Press():
    global current_state
    if current_state:
        Green.off()
        Red.off()
        print('Christmas over')
        current_state = False
    else:
        current_state = True
        turn_on()

def turn_on():
    global current_state
    print('Christmas Lights!')
    Red.blink(0.2,0.2)
    time.sleep(0.2)
    Green.blink(0.2,0.2)

button.when_pressed = Button_Press
# button.when_released = Button_Release

pause()
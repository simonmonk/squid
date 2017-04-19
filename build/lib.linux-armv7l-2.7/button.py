#squid.py Library

import RPi.GPIO as GPIO
import time

class Button:
    
    BUTTON_PIN = 0
    DEBOUNCE = 0
	
    def __init__(self, button_pin, debounce=0.05):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.BUTTON_PIN = button_pin
        self.DEBOUNCE = debounce

        GPIO.setup(self.BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
    def is_pressed(self):
        now = time.time()
        if GPIO.input(self.BUTTON_PIN) == False:
            time.sleep(self.DEBOUNCE)
            # wait for button release
            while not GPIO.input(self.BUTTON_PIN):
                pass
            return True
        return False
        

        


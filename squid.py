#squid.py Library

import RPi.GPIO as GPIO
import time

WHITE = (30, 30, 30)
OFF = (0, 0, 0)
RED = (100, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 100)
YELLOW = (50, 50, 0)
PURPLE = (50, 0, 50)
CYAN = (0, 50, 50)

class Squid:
	
    RED_PIN = 0
    GREEN_PIN = 0
    BLUE_PIN = 0

    red_pwm = 0
    green_pwm = 0
    blue_pwm = 0

    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.RED_PIN, self.GREEN_PIN, self.BLUE_PIN = red_pin, green_pin, blue_pin

        GPIO.setup(self.RED_PIN, GPIO.OUT)
        self.red_pwm = GPIO.PWM(self.RED_PIN, 500)
        self.red_pwm.start(0)
        
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)
        self.green_pwm = GPIO.PWM(self.GREEN_PIN, 500)
        self.green_pwm.start(0)
        
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)
        self.blue_pwm = GPIO.PWM(self.BLUE_PIN, 500)
        self.blue_pwm.start(0)
 
    def set_red(self, brightness):
        self.red_pwm.ChangeDutyCycle(brightness)
         
    def set_green(self, brightness):
        self.green_pwm.ChangeDutyCycle(brightness)
              
    def set_blue(self, brightness):
        self.blue_pwm.ChangeDutyCycle(brightness)
        
    def set_color(self, (r, g, b), brightness = 100):
        self.set_red(r * brightness / 100)
        self.set_green(g * brightness / 100)
        self.set_blue(b * brightness / 100)
        


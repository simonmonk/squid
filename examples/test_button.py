from button import *
import time

        
b = Button(7)

while True:
    if b.is_pressed():
        print(time.time())
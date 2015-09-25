from squid import *
import time

rgb = Squid(18, 23, 24)
rgb.set_color(RED)
time.sleep(2)
rgb.set_color(GREEN)
time.sleep(2)
rgb.set_color(BLUE)
time.sleep(2)
rgb.set_color(WHITE)
time.sleep(2)
rgb.set_color(WHITE, 300)
time.sleep(2)
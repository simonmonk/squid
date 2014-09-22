Squid
=====

# An RGB LED Python Library.

Squid is a Python library to drive the Raspberry Squid RGB LED. Or in fact any common cathode RGB LED.

The Raspberry Squid is an RGB LED with built-in series resistors and sockets that will plug directly onto the GPIO header of a Raspberry Pi.

![Raspberry Squid](http://www.simonmonk.org/wp-content/uploads/2014/09/squid_on_b_plus_1-web-1024x437.jpg)

# Installation

To install the library on your Raspberry Pi, enter the following commands in LX Terminal.

```
$ git clone https://github.com/simonmonk/squid.git
$ cd squid
$ sudo python setup.py install
```

# Connect the RGB LED

Plug in a Squid or connect up an RGB LED as follows:
+ Black, Common cathode of the LED to GND
+ Red squid lead to GPIO18
+ Green squid lead to GPIO23
+ Blue squid lead to GPIO24

# Try the Test Programs

There are two test programs, one (test.py) that simply turns the LED red, green, blue, white and then bright white. The other test program (gui.py) opens a TkInter window with three sliders to control the red, green and blue chanels of the LED.

First change to the examples directory using the command:

```
$ cd examples
```

To run **test** enter the following command:

```
$ sudo python test.py
```

To run **gui.py** enter the following command:

```
$ sudo python gui.py
```

This will open up the window below. Dragging the sliders about will allow you to mix any color.

![GUI Example]()


# API Documentation


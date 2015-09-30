Squid
=====

The Raspberry Squid is an open source hardware design for an RGB LED with built-in resistors and header lead sockets that can fit directly onto GPIO pins. If you don't want to make your own Squid, you can buy a ready made Raspberry Squid from http://www.monkmakes.com

The Squid has its own library to make it super easy to mix colors on the RGB LED. After the library documentation that follows, you will find instructions on how to create your own Squid.




# An RGB LED Python Library.

Squid is a Python library to drive the Raspberry Squid RGB LED. Or in fact any common cathode RGB LED. The library also includes code for switch debouncing. Something that uoi may find useful if you have the Raspberry Squid's companion the Raspberry Button.

The Raspberry Squid is an RGB LED with built-in series resistors and sockets that will plug directly onto the GPIO header of a Raspberry Pi.

![Raspberry Squid](http://www.simonmonk.org/wp-content/uploads/2014/09/squid_on_b_plus_1-web-1024x437.jpg)

The Raspberry Button follows the same concept, but has a push switch with protection resistor built into the leads.



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

![GUI Example](http://www.simonmonk.org/wp-content/uploads/2014/09/sliders_gui.png)


# API Documentation

You can probably find all you need to know by looking at the source code for the examples.  

## Importing the library

```
from squid import *
```


## Creating an Instance

```
rgb = Squid(18, 23, 24)
```

The three parameters are the pins connected tot he red, green and blue LEDs.



## set_color

```
rgb.set_color(RED)
```

The color can be one of the following constants: WHITE, OFF, RED, GREEN, BLUE, YELLOW, PURPLE and CYAN. 

You can also just provide a tuple containing R, G and B values each between 0 and 100, like this:

```
rgb.set_color((100, 50, 10))
```

An optional second argument allows you specify the brightness of the color. The value of 100 is equivalent to one of the LEDs only being on at full brightness, thus if you make your R, G and B values add up to 100, then you can reasonably set the brightness value between 0 and 300.

```
rgb.set_color(CYAN, 300)
```

## set_red(), set_green(), set_blue()

These methods allow you to set the three channels separately.

# Connect a Raspberry Button

Plug in a switch between the following pins (it does not matter which way around the leads are):
+ GND
+ GPIO 25

## Importing the library

```
from button import *
```


## Creating an Instance

```
button = Button(25)
```

The parameter is the pin that the button is connected to. There is also an optional second parameter of the debounce period (in seconds) to prevent false triggerings due to contact bouncing. 


```
button = Button(25, debounce=0.1)
```



## checking for button press

```
button.is_pressed()
```

This will return true if the button is pressed and will block and wait until the button has been released and the debounce period has elapsed.

Check out the example programs in the /examples folder of this library.


# How to Make Your Own Squid

## You will need

To make your own Squid, you will need the following parts:

+ An RGB common cathode diffuse LED (the bigger the better)
+ 3 x 470 Ohm resistors
+ Red, green, blue and black Female to Female jumper wires cut in half
+ 4 short lenths of heat shrink

You will also need soldering equipment and a hot air gun.

![Parts](http://simonmonk.org/wp-content/uploads/2015/04/01_parts-copy.jpg)

## Step 1. Prepare the LED

Leave the longest lead (common cathode) untouched, but trim the other leads as shown below.

![Preparing the LED](http://simonmonk.org/wp-content/uploads/2015/04/02_helping-hands-copy.jpg)

A apir of helping hands will - well - help.

## Step 2. Solder on the resistors

Trim the resistor leads and solder one end to each of the three short anode leads on the LED.

![Soldering the Resistors](http://simonmonk.org/wp-content/uploads/2015/04/04_soldering_r-copy.jpg)

When all the resistors are soldered, it will look like this.

![soldering the Resistors](http://simonmonk.org/wp-content/uploads/2015/04/05_soldering_resistors-copy.jpg)

## Step 3. Solder on the header wires

Slip the heat shrink sleaving over the wires BEFORE soldering the wires to the resistor wires and the common cathode. Use red for the red anode, green for bgreen and blue for blue and use a black wire for the common cathode.

![soldering the header wires](http://simonmonk.org/wp-content/uploads/2015/04/07_all_leads-copy.jpg)

## Step 4. Shrink the sleave

Push the heat shrink sleaves right up to the body of the LED and then shrink the wires using a hot air gun.

![shrinking the sleave](http://simonmonk.org/wp-content/uploads/2015/04/10_after_hot_air-copy.jpg)


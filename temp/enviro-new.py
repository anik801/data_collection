#!/usr/bin/env python3

import time
import colorsys
import os
import sys
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280
from enviroplus import gas
from subprocess import PIPE, Popen
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fonts.ttf import RobotoMedium as UserFont
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("""all-in-one.py - Displays readings from all of Enviro plus' sensors
Press Ctrl+C to exit!
""")

# BME280 temperature/pressure/humidity sensor
bme280 = BME280()

# Create LCD class instance.
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display.
disp.begin()

# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

# New canvas to draw on.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Text settings.
font_size = 8
font = ImageFont.truetype(UserFont, font_size)
text_colour = (255, 255, 255)
back_colour = (0, 170, 170)



prox1 = 0


# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE, universal_newlines=True)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])
    

# Tuning factor for compensation. Decrease this number to adjust the
# temperature down, and increase to adjust up
factor = 2.25
cpu_temps1 = [get_cpu_temperature()] * 5


delay = 0.5  # Debounce the proximity tap
mode = 0  # The starting mode
last_page = 0
light = 1

# Get the environment temperature
def get_temp(cpu_temps):
    unit = "C"
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    raw_temp = bme280.get_temperature()
    data = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
    data_t = "{:.2f}".format(data)
    t1 = "Temperature: " + str(data_t) + unit
    return (cpu_temps,t1)
    #display_text(variables[mode], data, unit)


# Get the proximity
def get_prox():
    pr1 = ltr559.get_proximity()
    pr1_format = "Proximity: " + str(pr1)
    return (pr1,pr1_format)
    
    
    
# Get the environment pressure
def get_pres():
    unit = "hPa"
    data = bme280.get_pressure()
    data_p = "{:.2f}".format(data)
    p1 = "Pressure: " + str(data_p) + unit
    return p1
    #display_text(variables[mode], data, unit)
    
    
# Get the environment humidity
def get_humi():
    unit = "%"
    data = bme280.get_humidity()
    data_h = "{:.2f}".format(data)
    h1 = "Humidity: " + str(data_h) + unit
    return h1
    #display_text(variables[mode], data, unit)

    
# Get light
def get_ligh():
    unit = "Lux"
    if prox1 < 10:
        data = ltr559.get_lux()
        data_l = "{:.2f}".format(data)
    else:
        data_l = 1
    l1 = "Light: " + str(data_l) + unit
    return l1
    #display_text(variables[mode], data, unit)


# Get gases
def get_gases():
       
    # variable = "oxidised"
    unit1 = "kO"
    data1 = gas.read_all()
    data1 = data1.oxidising / 1000
    data1_g = "{:.2f}".format(data1)
    #display_text(variables[mode], data1, unit1)


    # variable = "reduced"
    unit2 = "kO"
    data2 = gas.read_all()
    data2 = data2.reducing / 1000
    data2_g = "{:.2f}".format(data2)
    #display_text(variables[mode], data2, unit2)


    # variable = "nh3"
    unit3 = "kO"
    data3 = gas.read_all()
    data3 = data3.nh3 / 1000
    data3_g = "{:.2f}".format(data3)
    #display_text(variables[mode], data3, unit3)
    g = "Oxid: " + str(data1_g) + unit1 + ", Redu: " + str(data2_g) + unit2 + ", nh3: " + str(data3_g) + unit3
    return g

count=0


# The main loop
try:
    #while count<20:
    while True:
        count +=1
        
        gpr = get_prox()
        prox1 = gpr[0]
        gl = get_ligh()
        gt = get_temp(cpu_temps1)
        cpu_temps1 = gt[0]
        gp = get_pres()
        gh = get_humi()
        gg = get_gases()
        print(gpr[1])
        print(gl)
        print(gt[1])
        print(gp)
        print(gh)
        print(gg)
        
        message = gpr[1] + "\n" + gl + "\n" + gt[1] + "\n" + gp + "\n" + gh + "\n" + gg
        size_x, size_y = draw.textsize(message, font)

        # Calculate text position
        x = (WIDTH - size_x) / 2
        y = (HEIGHT / 2) - (size_y / 2)

        # Draw background rectangle and write text.
        draw.rectangle((0, 0, 160, 80), back_colour)
        draw.text((x, y), message, font=font, fill=text_colour)
        disp.display(img)

# Exit cleanly
except KeyboardInterrupt:
    sys.exit(0)




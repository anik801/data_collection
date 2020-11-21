# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:35:18 2020

@author: Sheik
"""
import time
import RPi.GPIO as GPIO
import datetime
import localdb

## field variables
local_data_dict = dict()


## TYPE 3 SENSOR CODES - CHANGE HERE IF NEEDED ##########################
##DHT11 SENSOR###########################################################
import Adafruit_DHT
dht_sensor = Adafruit_DHT.DHT11
dht_pin = 4
# returns temperature (centigrade) and humidity (percentage) readings 
def get_temperature_humidity():
    while True:
        humidity, temperature = Adafruit_DHT.read(dht_sensor, dht_pin)
        if humidity is not None and temperature is not None:
            return temperature, humidity
        
#def get_humidity():
#    humidity, _ = Adafruit_DHT.read(dht_sensor, dht_pin)
#    print(humidity)
#    return humidity
#########################################################################

##GAS SENSOR MQ2#########################################################
from mq import *
mq2 = None
def start_mq2_reading():
    global mq2
    if mq2 == None:
        mq2 = MQ()

def get_mq2_reading():
    global mq2
    reading = mq2.MQPercentage()
    return reading["SMOKE"], reading["CO"], reading["GAS_LPG"]
#########################################################################
## TYPE 3 SENSOR CODES - CHANGE HERE IF NEEDED ##########################


## method to get current date_time
## @return current date_time
def get_date_time():
    date_time = time.strftime('%Y-%m-%d %H:%M:%S')
    return date_time

## method to generate a record id
## @return the generated id
def get_id(rpi_id, date_time):
    row_id = date_time + "_" + rpi_id
    return row_id

## method to get reading of a callback sensor
## method resets local value of corresponding sensor
## @param sensor_pin refers to the pin sensor is connected with
def get_callback_reading(sensor_pin):
    data = local_data_dict[sensor_pin]
    local_data_dict[sensor_pin] = 0
    return data

## method to adjust readings in local_data_dict
## @param sensor_pin refers to the pin sensor is connected with
def sensor_callback(sensor_pin):
    data = local_data_dict[sensor_pin]
    local_data_dict[sensor_pin] = data + 1

## method to initialize callback sensors
## @param rpi_id refers to the corresponding raspberry pi 
def init_sensors(rpi_id):
    GPIO.setmode(GPIO.BCM)
    sensor_list = localdb.get_local_sensors(rpi_id)    
    for row in sensor_list:
        sensor_name = row[0]
        sensor_type = row[1]
        sensor_pin = row[2]
        if sensor_type == 1: ## direct input sensors             
            GPIO.setup(sensor_pin, GPIO.IN)
        elif sensor_type == 2: ##callback sensors
            GPIO.setup(sensor_pin, GPIO.IN)
            GPIO.add_event_detect(sensor_pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
            GPIO.add_event_callback(sensor_pin, sensor_callback)  # assign function to GPIO PIN, Run function on change
            local_data_dict[sensor_pin] = 0
        elif sensor_type == 3:
            ## CHANGE HERE IF NEEDED
            ## sensors that require special code 
            if sensor_name == "co" or sensor_name == "smoke" or sensor_name == "lpg": ## mq2 sensor
                start_mq2_reading()

## @param sensor_pin refers to the pin sensor is connected to in the rpi
## @param sensor_type refers to the specific type of the sensor
## @return the data of the corresponding sensor
def get_sensor_data(sensor_name, sensor_type, sensor_pin):
    data = None
    if sensor_type== 1: ## data can be directly read from the pin
        data = GPIO.input(sensor_pin)
    elif sensor_type == 2:        
        data = get_callback_reading(sensor_pin)
    elif sensor_type == 3:
        ## CHANGE HERE IF NEEDED
        ## sensors that require special code 
        if sensor_name == "temperature":
            data, _ = get_temperature_humidity()
        elif sensor_name == "humidity":
            _, data = get_temperature_humidity()
        elif sensor_name == "smoke":
            data, _, _ = get_mq2_reading()
        elif sensor_name == "co":
            _, data, _ = get_mq2_reading()
        elif sensor_name == "lpg":
            _, _, data = get_mq2_reading()
    return data
    
## method to get sensor readings
## @param rpi_id is the corresponding raspberry pi id
## @returns all sensor readings of the given rpi_id in dictionary format
def get_sensor_readings(rpi_id):
    date_time = get_date_time()
    data = dict()
    data['id'] = get_id(rpi_id, date_time)
    data['date_time'] = date_time
    data['rpi_id'] = rpi_id
    
    sensor_list = localdb.get_local_sensors(rpi_id)    
    for row in sensor_list:
        sensor_name = row[0]
        sensor_type = row[1]
        sensor_pin = row[2]
        
        reading = get_sensor_data(sensor_name, sensor_type, sensor_pin)
        data[sensor_name] = reading
#    print(data)
    return data


## TEST CODES; DELETE LATER
#init_sensors("1")
#get_sensor_readings("1")
#print(get_sensor_data(19, 1))


#########################################################################
## OLD METHODS ##########################################################
#########################################################################

###LIGHT SENSOR###########################################################
#light_pin = 19
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(light_pin,GPIO.IN)
## returns 0 for light and 1 for dark environment
#def get_light():
#    return GPIO.input(light_pin)
##########################################################################
#
###SOUND SENSOR############################################################
#sound_channel = 17
##GPIO.setmode(GPIO.BCM) #already done
#GPIO.setup(sound_channel, GPIO.IN)
#sound_beat = 0
#def sound_callback(sound_channel):
#    global sound_beat
#    sound_beat = sound_beat + 1
#    
#def start_sound_reading():
#    GPIO.add_event_detect(sound_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#    GPIO.add_event_callback(sound_channel, sound_callback)  # assign function to GPIO PIN, Run function on change
#    
#def get_sound():
#    global sound_beat
#    beat = sound_beat
#    sound_beat = 0
#    return beat
##########################################################################
#
####VIBRATION SENSOR######################################################
#vibration_channel = 16
##GPIO.setmode(GPIO.BCM) #already done
#GPIO.setup(vibration_channel, GPIO.IN)
#vibration_beat = 0
#def vibration_callback(vibration_channel):
#    global vibration_beat
#    vibration_beat = vibration_beat + 1
#    
#def start_vibration_reading():
#    GPIO.add_event_detect(vibration_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#    GPIO.add_event_callback(vibration_channel, vibration_callback)  # assign function to GPIO PIN, Run function on change
#    
#def get_vibration():
#    global vibration_beat
#    beat = vibration_beat
#    vibration_beat = 0
#    return beat
##########################################################################
#
###PIR SENSOR#############################################################
#pir_pin = 23
#motion_beat = 0
##GPIO.setmode(GPIO.BCM) # already done
#GPIO.setup(pir_pin, GPIO.IN) #PIR
#def get_motion():
#    global motion_beat
#    beat = motion_beat
#    motion_beat = 0
#    return beat
#
#def start_motion_reading():
#    motion_thread = threading.Thread(target = check_motion)
#    motion_thread.start()
#
#def check_motion():
#    global motion_beat
#    while True:
#        if GPIO.input(pir_pin):
#            motion_beat = motion_beat + 1
#        time.sleep(0.1) # loop delay
#        
### alternate implementation of motion sensor
##def motion_callback(pir_pin):
##    global motion_beat
##    motion_beat = motion_beat + 1
##    
##def start_motion_reading():
##    GPIO.add_event_detect(pir_pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
##    GPIO.add_event_callback(pir_pin, motion_callback)  # assign function to GPIO PIN, Run function on change
##########################################################################
#
###FLAME SENSOR###########################################################
#flame_channel = 12
##GPIO.setmode(GPIO.BCM) #already done
#GPIO.setup(flame_channel, GPIO.IN)
#flame_beat = 0
#def flame_callback(flame_channel):
#    global flame_beat
#    flame_beat = flame_beat + 1
#    
#def start_flame_reading():
#    GPIO.add_event_detect(flame_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#    GPIO.add_event_callback(flame_channel, flame_callback)  # assign function to GPIO PIN, Run function on change
#    
#def get_flame():
#    global flame_beat
#    beat = flame_beat
#    flame_beat = 0
#    return beat
##########################################################################
#
#
### method to get sensor readings
### @param rpi_id refers to the raspberry pi
### @return sensor readings in dictionary format
#def get_reading(rpi_id):
#    date_time = get_date_time()
#    row = dict()
#    row['id'] = get_id(rpi_id, date_time)
#    row['date_time'] = date_time
#    row['rpi_id'] = rpi_id
#    row['temp'], row['humidity'] = get_temperature_humidity()
#    row['light'] = get_light()
#    row['sound'] = get_sound()
#    row['flame'] = get_flame()
#    row['vibration'] = get_vibration()
#    row['motion'] = get_motion()
#    row['smoke'], row['co'], row['lpg'] = get_mq2_reading()
#    
#    return row
##########################################################################
import Adafruit_DHT
import time
import datetime
import RPi.GPIO as GPIO
import threading
import datetime
from mq import *

##DHT11 SENSOR###########################################################
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

##LIGHT SENSOR###########################################################
light_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_pin,GPIO.IN)
# returns 0 for light and 1 for dark environment
def get_light():
    return GPIO.input(light_pin)
#########################################################################

##SOUND SENSOR############################################################
sound_channel = 17
#GPIO.setmode(GPIO.BCM) #already done
GPIO.setup(sound_channel, GPIO.IN)
sound_beat = 0
def sound_callback(sound_channel):
    global sound_beat
    sound_beat = sound_beat + 1
    
def start_sound_reading():
    GPIO.add_event_detect(sound_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(sound_channel, sound_callback)  # assign function to GPIO PIN, Run function on change
    
def get_sound():
    global sound_beat
    beat = sound_beat
    sound_beat = 0
    return beat
#########################################################################

###VIBRATION SENSOR######################################################
vibration_channel = 16
#GPIO.setmode(GPIO.BCM) #already done
GPIO.setup(vibration_channel, GPIO.IN)
vibration_beat = 0
def vibration_callback(vibration_channel):
    global vibration_beat
    vibration_beat = vibration_beat + 1
    
def start_vibration_reading():
    GPIO.add_event_detect(vibration_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(vibration_channel, vibration_callback)  # assign function to GPIO PIN, Run function on change
    
def get_vibration():
    global vibration_beat
    beat = vibration_beat
    vibration_beat = 0
    return beat
#########################################################################

##PIR SENSOR#############################################################
pir_pin = 23
motion_beat = 0
#GPIO.setmode(GPIO.BCM) # already done
GPIO.setup(pir_pin, GPIO.IN) #PIR
def get_motion():
    global motion_beat
    beat = motion_beat
    motion_beat = 0
    return beat

def start_motion_reading():
    motion_thread = threading.Thread(target = check_motion)
    motion_thread.start()

def check_motion():
    global motion_beat
    while True:
        if GPIO.input(pir_pin):
            motion_beat = motion_beat + 1
        time.sleep(0.1) # loop delay
        
## alternate implementation of motion sensor
#def motion_callback(pir_pin):
#    global motion_beat
#    motion_beat = motion_beat + 1
#    
#def start_motion_reading():
#    GPIO.add_event_detect(pir_pin, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#    GPIO.add_event_callback(pir_pin, motion_callback)  # assign function to GPIO PIN, Run function on change
#########################################################################

##VIBRATION SENSOR#######################################################
flame_channel = 12
#GPIO.setmode(GPIO.BCM) #already done
GPIO.setup(flame_channel, GPIO.IN)
flame_beat = 0
def flame_callback(flame_channel):
    global flame_beat
    flame_beat = flame_beat + 1
    
def start_flame_reading():
    GPIO.add_event_detect(flame_channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(flame_channel, flame_callback)  # assign function to GPIO PIN, Run function on change
    
def get_flame():
    global flame_beat
    beat = flame_beat
    flame_beat = 0
    return beat
#########################################################################

##GAS SENSOR MQ2#########################################################
mq2 = None
def start_mq2_reading():
    global mq2
    mq2 = MQ()

def get_mq2_reading():
    global mq2
    reading = mq2.MQPercentage()
    return reading["SMOKE"], reading["CO"], reading["GAS_LPG"]
#########################################################################

##HELPER METHODS#########################################################
def get_date_time():
    date_time = str(datetime.datetime.now())
    return date_time

def get_id(rpi_id, room_id, date_time):
    row_id = date_time + "_" + rpi_id + "_" + room_id
    return row_id
    
def get_reading(rpi_id, room_id):
    date_time = get_date_time()
    row = dict()
    row['id'] = get_id(rpi_id, room_id, date_time)
    row['date_time'] = date_time
    row['rpi_id'] = rpi_id
    row['room_id'] = room_id
    row['temp'], row['humidity'] = get_temperature_humidity()
    row['light'] = get_light()
    row['sound'] = get_sound()
    row['flame'] = get_flame()
    row['vibration'] = get_vibration()
    row['motion'] = get_motion()
    row['smoke'], row['co'], row['lpg'] = get_mq2_reading()
    
    return row
#########################################################################

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:51:52 2020

@author: John
"""

import datetime

def get_temp():
    data = 22
    return data

def get_humidity():
    data = 67
    return data

def get_light():
    data = 0
    return data

def get_sound():
    data = 0
    return data

def get_flame():
    data = 0 
    return data

def get_vibration():
    data = 0 
    return data

def get_motion():
    data = 1
    return data

def get_smoke():
    data = 0 
    return data

def get_CO():
    data = 1
    return data

def get_natural_gas():
    data = 1
    return data

def get_date_time():
    date_time = str(datetime.datetime.now())
    return date_time

def get_id(rpi_id, room_id, date_time):
    row_id = rpi_id + "_" + room_id + "_" + date_time
    return row_id
    
def get_reading(rpi_id, room_id):
    date_time = get_date_time()
    row = dict()
    row['id'] = get_id(rpi_id, room_id, date_time)
    row['date_time'] = date_time
    row['temp'] = get_temp()
    row['humidity'] = get_humidity()
    row['light'] = get_light()
    row['sound'] = get_sound()
    row['flame'] = get_flame()
    row['vibration'] = get_vibration()
    row['motion'] = get_motion()
    row['smoke'] = get_smoke()
    row['co'] = get_CO()
    row['natural_gas'] = get_natural_gas()
    
    return row
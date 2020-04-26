# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:35:18 2020

@author: John
"""

## importing libraries
import sensors
import server
import localdb
import time
from timeloop import Timeloop
from datetime import timedelta

## field variables
rpi_id = "m1" ## raspberry pi id should different should each module
room_id = "r1" ## room id should be different for each room
time_loop = Timeloop()
start_time = time.time()

## change timings here
LOCAL_SERVER_TIME_INTERVAL = 60 # seconds
CENTRAL_SERVER_TIME_INTERVAL = 3600 # seconds

## method to collect and store data in local database
## call every 1 minute
@time_loop.job(interval=timedelta(seconds=LOCAL_SERVER_TIME_INTERVAL))
def localdb_routine():
#    print("local_routine")
    try:
        reading = sensors.get_reading(rpi_id, room_id)
        localdb.store_data(reading)
    except:
        print("Exception in local_routine")

## method to store data to central server
## call every 1 hour
@time_loop.job(interval=timedelta(seconds=CENTRAL_SERVER_TIME_INTERVAL))
def server_routine():
#    print("SERVER ROUTINE")
    last_date_time = server.get_latest_entry(rpi_id, room_id)
    file_name = localdb.extract_to_csv(last_date_time, rpi_id, room_id) ## sends data to server
    server.sendFile(file_name)
    
## prepare sensors for reading
def initiate_sensors():
    global sensors
    sensors.start_sound_reading()
    sensors.start_vibration_reading()
    sensors.start_motion_reading()
    sensors.start_flame_reading()
    sensors.start_mq2_reading()

## start program execution 
def main():
    print("Running Local Module")
    initiate_sensors()
    time_loop.start()
 
###############################################################
    ## enable the following part for limited time eecution
    ## stop the program after certain time 
#    runtime = 100 ## seconds
#    while True:    
#        new_time = time.time()
#        time_diff = new_time - start_time
##        print(time_diff)  #show timer
#        if(time_diff > runtime):
#            time_loop.stop()
#            break
#        time.sleep(1)
###############################################################

def testFunction():
    last_date_time = server.get_latest_entry(rpi_id, room_id)
    file_name = localdb.extract_to_csv(last_date_time, rpi_id, room_id) ## sends data to server
    print(file_name)

## define main method call
if __name__ == "__main__":
    main()
#    testFunction()
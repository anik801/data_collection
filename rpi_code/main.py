# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:35:18 2020

@author: Sheik
"""

## importing libraries
import sensors
import server
import localdb
import time
from timeloop import Timeloop
from datetime import timedelta

## field variables
rpi_id = "1" ## raspberry pi id should different should each module
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
    rpi_status = server.check_rpi_status(rpi_id)
    if rpi_status == "1": 
        ## table in central database has been updated
        localdb.sync_db(rpi_id)
    else:    
        try:
#            reading = sensors.get_reading(rpi_id)
            reading = sensors.get_sensor_readings(rpi_id)
            localdb.store_data(reading)
        except:
            error_date_time = sensors.get_date_time()
            error_message = error_date_time + " Exception in local_routine"
            localdb.log_error(rpi_id, error_date_time, error_message)

## method to store data to central server
## call every 1 hour
@time_loop.job(interval=timedelta(seconds=CENTRAL_SERVER_TIME_INTERVAL))
def server_routine():
#    print("SERVER ROUTINE")
    try: 
        last_date_time = server.get_latest_entry(rpi_id)
        file_name = localdb.extract_to_csv(last_date_time, rpi_id) ## sends data to server
        server.send_file(file_name)
        # TODO: sync error log
    except:
        error_date_time = sensors.get_date_time()
        error_message = error_date_time + " Exception in server_routine"
        localdb.log_error(rpi_id, error_date_time, error_message)
        
    
### prepare sensors for reading
#def initiate_sensors():
#    global sensors
#    sensors.start_sound_reading()
#    sensors.start_vibration_reading()
#    sensors.start_motion_reading()
#    sensors.start_flame_reading()
#    sensors.start_mq2_reading()

## start program execution 
def main():
    print("Running Local Module")
    localdb.init_db(rpi_id)
#    initiate_sensors()
    sensors.init_sensors(rpi_id)
    time_loop.start(block=True)
    ## TODO: sync error log
 
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
    print("Test Function")
#     last_date_time = server.get_latest_entry(rpi_id)
#     file_name = localdb.extract_to_csv(last_date_time, rpi_id) ## sends data to server
#         
#     print(file_name)
    
#     server.get_sensor_list(rpi_id)
#     localdb.sync_db(rpi_id)
#     sensors.init_sensors(rpi_id)
#     localdb_routine();
#     reading = sensors.get_sensor_readings(rpi_id)
#     print("data:")
#     print(reading)
    

## define main method call
if __name__ == "__main__":
    main()
#     testFunction()
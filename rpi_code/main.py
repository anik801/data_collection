# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 21:35:18 2020

@author: John
"""

#import threading
#
#def printit():
#  threading.Timer(5.0, printit).start()
#  print ("Hello, World!")
#
#printit()

import sensors
import server
import localdb
#import threading

import time
from timeloop import Timeloop
from datetime import timedelta

rpi_id = "m1"
room_id = "r1"
time_loop = Timeloop()
start_time = time.time()

## method to collect and store data in local database
## call every 1 minute

@time_loop.job(interval=timedelta(seconds=6))
def localdb_routine():
#    print("local_routine")
#    check_timer()
#    threading.Timer(1.0, localdb_routine).start()
    reading = sensors.get_reading(rpi_id, room_id)
    localdb.store_data(reading, rpi_id, room_id)

## method to store data to central server
## call every 1 hour
@time_loop.job(interval=timedelta(seconds=30))
def server_routine():
#    print("SERVER ROUTINE")
#    check_timer()
#    threading.Timer(60.0, server_routine).start()
    last_date_time = server.get_latest_entry(rpi_id, room_id)
    localdb.save_latest_data(last_date_time, rpi_id, room_id) ##sends data to server


    
def main():
    print("Running Local Module")
    time_loop.start()
 
    ## enable the following part for limited time eecution
    ## stop the program after certain time 
    runtime = 100 ## seconds
    while True:    
        new_time = time.time()
        time_diff = new_time - start_time
        print(time_diff)
        if(time_diff > runtime):
            time_loop.stop()
            break
        time.sleep(1)
    

    
#    date_time = "2020-03-25 20:18:36.658665"
#    save_latest_data(date_time)
    
#    temp_id = "natural_gas_m1_r1_2020-03-25 21:04:36.856393"
#    temp_date_time = "2020-03-25 21:04:36.856392"
#    temp_rpi_id = "m1"
#    temp_room_id = "r1"
#    temp_sensor = "natural_gas"
#    temp_data = "1"
#    ## store row in central database
#    send_to_server(temp_id, temp_date_time, temp_rpi_id, temp_room_id, temp_sensor, temp_data)
    
    
    
    

    
    
def tempFoo():
    print("Running Temp Foo")   
    
    

        
if __name__ == "__main__":
#    main()
    tempFoo()
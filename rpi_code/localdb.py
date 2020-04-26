# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:12:52 2020

@author: John
"""

## importing libraries
import mysql.connector as mariadb
import server
import time
import csv

## method to get connection to local database
## @return connection
def mariadb_con():
    mariadb_connection = mariadb.connect(user='root', password='root_password', database='local_data')
    cursor = mariadb_connection.cursor()    
    return mariadb_connection, cursor     

## method to store data in local database    
## @param reading is the current reading 
def store_data(reading):
    key_str = ""
    value_str = ""
    i = 0
    key_len = len(reading)
    for key in reading.keys():
        if i < key_len - 1:
            key_str = key_str + "`" + key + "`,"
            value_str = value_str + "'" + str(reading[key]) + "',"
        else:
            key_str = key_str + "`" + key + "`"
            value_str = value_str + "'" + str(reading[key]) + "'"
        i = i + 1
    mariadb_connection, cursor = mariadb_con()
    sql = "INSERT INTO `storage_v2`(" + key_str + ") VALUES (" + value_str +")"
    cursor.execute(sql)
    mariadb_connection.commit()
                
## method export latest data in a csv file
## @param date_time is the last available date_time in the server given rpi_id and room_id
## return name of the generated csv file
def extract_to_csv(date_time, rpi_id, room_id):
    file_name = rpi_id + "_" + room_id + ".csv"
    mariadb_connection, cursor = mariadb_con()
    sql = "SELECT * FROM `storage_v2` WHERE (`rpi_id`='"+rpi_id+"' AND `room_id`='"+room_id+"' AND `date_time`>'"+date_time+"')"
    cursor.execute(sql)
    
    rows=cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    fp = open(file_name, 'w')
    file = csv.writer(fp, lineterminator = '\n')
    file.writerow(column_names)   
    file.writerows(rows)
    fp.close()
    return file_name






###############################################################################################
## Old Methods ################################################################################
###############################################################################################
#
#def mariadb_con():
#    mariadb_connection = mariadb.connect(user='root', password='root_password', database='local_data')
#    cursor = mariadb_connection.cursor()    
#    return mariadb_connection, cursor    
#    
#def local_db_insert(row_id, date_time, rpi_id, room_id, sensor, data):
#    mariadb_connection, cursor = mariadb_con()
#    sql = "INSERT INTO `storage`(`id`, `date_time`, `rpi_id`, `room_id`, `sensor`, `data`) VALUES ('"+ str(row_id) +"', '"+ str(date_time) +"', '"+ str(rpi_id) +"', '"+ str(room_id) +"', '"+ str(sensor) +"', '"+ str(data) +"')"
#    cursor.execute(sql)
#    mariadb_connection.commit()
#    
#def already_present(row_id):
#    mariadb_connection, cursor = mariadb_con()
#    sql = "SELECT * FROM `storage` WHERE (`id`='"+row_id+"')"
#    cursor.execute(sql)
#    cursor.fetchall()
#    return cursor.rowcount > 0
#
#def store_data(reading, rpi_id, room_id):
#    reading_id = reading['id']
#    date_time = reading['date_time']
#    
#    for key in reading.keys():
#        row_id = reading_id + '_' + key
#        if key == 'id' or key == 'rpi_id' or key == 'room_id' or key == 'date_time': ## skip auxilary information            
#            continue
#        if already_present(row_id): ## avoid duplicate entry
#            continue
#        local_db_insert(row_id, date_time, rpi_id, room_id, key, reading[key])
#        
### send latest data to server
### @param date_time is the last available date_time in the server given rpi_id and room_id
#def save_latest_data(date_time, rpi_id, room_id):
#    mariadb_connection, cursor = mariadb_con()
#    sql = "SELECT * FROM `storage` WHERE (`rpi_id`='"+rpi_id+"' AND `room_id`='"+room_id+"' AND `date_time`>'"+date_time+"')"
#    cursor.execute(sql)
#    for row in cursor:
#        temp_id = row[0]
#        temp_date_time = date_time = row[1]
#        temp_rpi_id = row[2]
#        temp_room_id = row[3]
#        temp_sensor = row[4]
#        temp_data = row[5]
#        ## store row in central database
#        try:
#            server.store_data(temp_id, temp_date_time, temp_rpi_id, temp_room_id, temp_sensor, temp_data)
#        except:
#            time.sleep(10) #wait 5 seconds if server refuses connection
#            save_latest_data(date_time, rpi_id, room_id)
#        time.sleep(1) # put a delay between server calls

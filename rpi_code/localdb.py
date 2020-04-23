# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:12:52 2020

@author: John
"""
import mysql.connector as mariadb
import server

def mariadb_con():
    mariadb_connection = mariadb.connect(user='root', password='root_password', database='local_data', port = 3307)
    cursor = mariadb_connection.cursor()    
    return mariadb_connection, cursor    
    
def local_db_insert(row_id, date_time, rpi_id, room_id, sensor, data):
    mariadb_connection, cursor = mariadb_con()
    sql = "INSERT INTO `storage`(`id`, `date_time`, `rpi_id`, `room_id`, `sensor`, `data`) VALUES ('"+ str(row_id) +"', '"+ str(date_time) +"', '"+ str(rpi_id) +"', '"+ str(room_id) +"', '"+ str(sensor) +"', '"+ str(data) +"')"
    cursor.execute(sql)
    mariadb_connection.commit()
    
def already_present(row_id):
    mariadb_connection, cursor = mariadb_con()
    sql = "SELECT * FROM `storage` WHERE (`id`='"+row_id+"')"
    cursor.execute(sql)
    cursor.fetchall()
    return cursor.rowcount > 0

def store_data(reading, rpi_id, room_id):
    reading_id = reading['id']
    date_time = reading['date_time']
    
    for key in reading.keys():
        row_id = key+'_' + reading_id
        if key == 'id' or key == 'rpi_id' or key == 'room_id' or key == 'date_time': ## skip auxilary information            
            continue
        if already_present(row_id): ## avoid duplicate entry
            continue
        local_db_insert(row_id, date_time, rpi_id, room_id, key, reading[key])
        
## send latest data to server
## @param date_time is the last available date_time in the server given rpi_id and room_id
def save_latest_data(date_time, rpi_id, room_id):
    mariadb_connection, cursor = mariadb_con()
    sql = "SELECT * FROM `storage` WHERE (`rpi_id`='"+rpi_id+"' AND `room_id`='"+room_id+"' AND `date_time`>'"+date_time+"')"
    cursor.execute(sql)
    for row in cursor:
        temp_id = row[0]
        temp_date_time = date_time = row[1]
        temp_rpi_id = row[2]
        temp_room_id = row[3]
        temp_sensor = row[4]
        temp_data = row[5]
        ## store row in central database
        server.store_data(temp_id, temp_date_time, temp_rpi_id, temp_room_id, temp_sensor, temp_data)
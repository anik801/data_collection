# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:12:52 2020

@author: Sheik
"""

## importing libraries
import mysql.connector as mariadb
import server
import csv
import json

## method to execute SQL script
## @param filename is the name of sql file
def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    mariadb_connection = mariadb.connect(user='root', password='root_password')
    cursor = mariadb_connection.cursor(buffered=True)    
    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except Exception as ex:
            print ("Command skipped: ", ex)
    cursor.close()
            
## method to get connection to local database
## @return connection
def mariadb_con():
    try:
        mariadb_connection = mariadb.connect(user='root', password='root_password', database='local_data')
        cursor = mariadb_connection.cursor(buffered=True)    
        return mariadb_connection, cursor
    except Exception as ex:
        print("Local database connection exception: ", ex)
        return None, None

## method to initialize local database
def init_db(rpi_id):
    mariadb_connection, cursor = mariadb_con()
    print(mariadb_connection, cursor)
    if mariadb_connection == None:
        executeScriptsFromFile('local_data.sql')
    sync_db(rpi_id)        

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
    cursor.close()
                
## method export latest data in a csv file
## @param date_time is the last available date_time in the server given rpi_id and room_id
## return name of the generated csv file
def extract_to_csv(date_time, rpi_id):
    file_name = rpi_id + ".csv"
    mariadb_connection, cursor = mariadb_con()
#    sql = "SELECT * FROM `storage_v2` WHERE (`rpi_id`='"+rpi_id+"' AND `date_time`>'"+date_time+"')" ## ENABLE THIS
    sql = "SELECT * FROM `storage_v2` WHERE (`rpi_id`='"+rpi_id+"' AND `date_time`>'"+date_time+"')"
    cursor.execute(sql)
    
    rows=cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    fp = open(file_name, 'w')
    file = csv.writer(fp, lineterminator = '\n')
    file.writerow(column_names)   
    file.writerows(rows)
    fp.close()
    cursor.close()
    return file_name



## method to check if a sensor is present in the local database
## @param rpi_id is the raspberry pi id and sensor is the sensor to find
## @return true if match found and false otherwise
def find_sensor_in_local_db(rpi_id, sensor):
    mariadb_connection, cursor = mariadb_con()
    sql = "SELECT `sensor` FROM `sensors` WHERE (`rpi_id`='"+rpi_id+"' AND `sensor`='"+sensor+"');"
    cursor.execute(sql)
    cursor.fetchall()
    result = cursor.rowcount > 0
    cursor.close()
    return result

## method to check if a sensor is present in a list
## @param data is the list of sensors
## @param sensor_name, sensor_type, sensor_pin is corresponding information to match
## @return true if match found and false otherwise
def find_match_in_data(data, sensor_name, sensor_type, sensor_pin):
    for row in data:
        if row['sensor'] == sensor_name and row['type'] == str(sensor_type) and row['pin'] == str(sensor_pin):
            return True
    return False

## method to synchronize local database with central server
## param rpi_id refers to the current raspberry pi id
def sync_db(rpi_id):
    sensor_info = server.get_sensor_list(rpi_id);
#     print(sensor_info)
#    temp_sensor_info = '[{"sensor": "co", "type": "1", "pin": "1"}, {"sensor": "flame", "type": "1", "pin": "1"}, {"sensor": "humidity", "type": "1", "pin": "1"}, {"sensor": "light", "type": "1", "pin": "1"}, {"sensor": "lpg", "type": "1", "pin": "1"}, {"sensor": "motion", "type": "1", "pin": "1"}, {"sensor": "smoke", "type": "1", "pin": "1"}, {"sensor": "sound", "type": "1", "pin": "1"}, {"sensor": "temp", "type": "1", "pin": "1"}, {"sensor": "vibration", "type": "1", "pin": "1"}]'
#    updated_sensors = json.dumps(temp_sensor_info)
    updated_sensors = json.loads(sensor_info)

    mariadb_connection, cursor = mariadb_con()
    mariadb_connection_2, cursor_2 = mariadb_con()
    sql = "SELECT `sensor`, `type`, `pin` FROM `sensors` WHERE `rpi_id`='"+rpi_id+"' ORDER BY `sensor`"
    cursor.execute(sql)
    for row in cursor:
        sensor_name = row[0]
        sensor_type = row[1]
        sensor_pin = row[2]
        
        if not find_match_in_data(updated_sensors, sensor_name, sensor_type, sensor_pin):
            sql_2 = "DELETE FROM `sensors` WHERE (`rpi_id`='"+rpi_id+"' AND `sensor`='"+sensor_name+"');"
            cursor_2.execute(sql_2)
            sql_2 = "ALTER TABLE `storage_v2` DROP COLUMN `"+sensor_name+"`;"
            cursor_2.execute(sql_2)
            mariadb_connection_2.commit()
    for row in updated_sensors:
        sensor_name = row['sensor']
        sensor_type = row['type']
        sensor_pin = row['pin']
                
        if not find_sensor_in_local_db(rpi_id, sensor_name):
            sql_2 = "INSERT INTO `sensors` (`rpi_id`,`sensor`,`type`,`pin`) VALUES ('"+rpi_id+"', '"+sensor_name+"', '"+sensor_type+"', '"+sensor_pin+"');"            
            cursor_2.execute(sql_2)
            sql_2 = "ALTER TABLE `storage_v2` ADD COLUMN `"+sensor_name+"` double DEFAULT NULL;"
            cursor_2.execute(sql_2)
            mariadb_connection_2.commit()
    server.update_rpi_status(rpi_id)
    cursor.close()
    cursor_2.close()

## method to get local sensor information
## @param rpi_id is the corresponding raspberry pi id
## @return sensor information 
def get_local_sensors(rpi_id):
    mariadb_connection, cursor = mariadb_con()
    sql = "SELECT `sensor`, `type`, `pin` FROM `sensors` WHERE `rpi_id`='"+rpi_id+"';"
    cursor.execute(sql)
    sensor_data = cursor.fetchall()
    cursor.close()
    return sensor_data

## method to log error in local database
def log_error(rpi_id, date_time, error_message):
    print(error_message)
    mariadb_connection, cursor = mariadb_con()
    sql = "INSERT INTO `error_log`(`rpi_id`, `date_time`, `message`) VALUES ('"+rpi_id+"', '"+date_time+"', '"+error_message+"');"
    cursor.execute(sql)
    mariadb_connection.commit()
    cursor.close()
    ## TODO: add in local db
    
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

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:09:10 2020

@author: Sheik
"""

## importing libraries
import requests

## field variables
# server_url = "http://192.168.0.6/data_collection/"
server_url = "https://building-data-lite.com/"

## method to get the latest entry in local database of given rpi and room 
## @param rpi_id is given to find require information
## @return date_time of last insterted row
def get_latest_entry(rpi_id):
    row_data = {"rpi_id": rpi_id}
    url = server_url + "get_latest_entry.php"
    headers = {"User-Agent": "Mozilla Firefox"}
    response = requests.post(url=url, params=row_data, headers=headers)
  
#     response = requests.post(url, params=row_data)
#    print(resp.text)
    return response.text

## method to send file to central server
## @param file_name contains rpi_id and room_id
def send_file(file_name):
    url = server_url + "file_receive.php"
    files = {'file': open(file_name, 'rb')}
    headers = {"User-Agent": "Mozilla Firefox"}
    r = requests.post(url=url, files=files, headers=headers)
    
#     r = requests.post(url, files=files)
    if r.text == "1":
        print("Error uploading file\n")
        ## TODO: insert error in error log
#    print(r.text)

## method to get the rpi status from
## @param rpi_id is the current rpi_id
## @return 1 if rpi has been modified and 0 otherwise
def check_rpi_status(rpi_id):
    row_data = {"rpi_id": rpi_id}
    url = server_url + "get_rpi_status.php"
    headers = {"User-Agent": "Mozilla Firefox"}
    response = requests.post(url=url, params=row_data, headers=headers)
    
#     response = requests.post(url, params=row_data)
    return response.text

def update_rpi_status(rpi_id):
    row_data = {"rpi_id": rpi_id}
    url = server_url + "update_rpi_status.php"
    headers = {"User-Agent": "Mozilla Firefox"}
    response = requests.post(url=url, params=row_data, headers=headers)
    
#     response = requests.post(url, params=row_data)
    
    
## method to get sensor list from server 
## @param rpi_id id will be sent to the server
## @return sensor list in json format done in php
def get_sensor_list(rpi_id):
    row_data = {"rpi_id": rpi_id}
    headers = {"User-Agent": "Mozilla Firefox"}
    url = server_url + "get_sensor_list_of_rpi.php"
    response = requests.post(url=url, params=row_data, headers=headers)
    return response.text



###############################################################################################
## Old Methods ################################################################################
###############################################################################################
#
#import requests
#
#server_url = "http://192.168.0.6/data_collection/"
#
### @param rpi_id and room_id are given to find require information
### @return date_time of last insterted row
#def get_latest_entry(rpi_id, room_id):
#    row_data = {"rpi_id": rpi_id, "room_id": room_id}
#    url = server_url + "get_latest_entry.php"
#    response = requests.post(url, params=row_data)
##    print(resp.text)
#    return response.text
#
### @param row data    
### send one row to php server 
#def store_data(row_id, date_time, rpi_id, room_id, sensor, data):
#    row_data = {"row_id": row_id, "date_time": date_time, "rpi_id": rpi_id, "room_id": room_id, "sensor": sensor, "data": data}
#    url = server_url + "receive_data.php"
#    response = requests.post(url, params=row_data)
#    if response.text != "0":
#        print("Failed to send data to server; row_id: " + row_id)
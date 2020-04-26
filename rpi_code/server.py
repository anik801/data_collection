# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:09:10 2020

@author: John
"""

import requests

server_url = "http://192.168.0.6/data_collection/"

## method to get the latest entry in local database of given rpi and room 
## @param rpi_id and room_id are given to find require information
## @return date_time of last insterted row
def get_latest_entry(rpi_id, room_id):
    row_data = {"rpi_id": rpi_id, "room_id": room_id}
    url = server_url + "get_latest_entry.php"
    response = requests.post(url, params=row_data)
#    print(resp.text)
    return response.text

## send one row to php server 
## @param row data    
def store_data(row_id, date_time, rpi_id, room_id, sensor, data):
    row_data = {"row_id": row_id, "date_time": date_time, "rpi_id": rpi_id, "room_id": room_id, "sensor": sensor, "data": data}
    url = server_url + "receive_data.php"
    response = requests.post(url, params=row_data)
    if response.text != "0":
        print("Failed to send data to server; row_id: " + row_id)

## method to send file to central server
## @param file_name contains rpi_id and room_id
def sendFile(file_name):
    url = server_url + "file_receive.php"
    files = {'file': open(file_name, 'rb')}
    r = requests.post(url, files=files)
    if r.text == "1":
        print("Error uploading file\n")
#    print(r.text)
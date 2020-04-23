# -*- coding: utf-8 -*-
"""
Created on Mon Sep 09 00:51:31 2019

@author: John
"""

## send 

#import requests
#userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
#resp = requests.post('http://192.168.0.11/data_collection/index.php', params=userdata)
#print(resp)


### read
#
#import json
#import urllib.request
#url = "http://192.168.0.6/data_collection/index.php"
#x = urllib.request.urlopen(url)
#raw_data = x.read()
#encoding = x.info().get_content_charset('utf8')  # JSON default
#print(raw_data)   #this is data in string format
##data = json.loads(raw_data.decode(encoding))
##print(data)   #this would be your json data


## thread

#import threading
#
#def printit():
#  threading.Timer(5.0, printit).start()
#  print ("Hello, World!")
#
#printit()

import time

from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(seconds=2))
def sample_job_every_2s():
    print ("2s job current time : {}".format(time.ctime()))

@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    print ("5s job current time : {}".format(time.ctime()))


@tl.job(interval=timedelta(seconds=10))
def sample_job_every_10s():
    print ("10s job current time : {}".format(time.ctime()))
    
    
tl.start()

i = 1

while True:
    i = i + 1
    if i > 10:
        tl.stop()
        break
    time.sleep(1)
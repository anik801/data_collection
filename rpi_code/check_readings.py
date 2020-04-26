import test
import sensors
import time
#import datetime
#import csv

# main function body
def main():
    # welcome message 
    print("Main function running. Welcome to the system.")
    
    # check sensor data
    #test.sensor_test()
#    temperature, humidity = sensors.get_temperature_humidity() 
#    print(temperature, humidity) #centigrade, percentage
#    
#    light = sensors.get_light() #1: Dark; 0:light
#    print(light)

    reading_interval = 5 # seconds
    sensors.start_sound_reading()
    sensors.start_vibration_reading()
    sensors.start_motion_reading()
    sensors.start_flame_reading()
    sensors.start_mq2_reading()
    
#    time.sleep(2) # 2 second delay to stabilize sensors
    
    while True:
        temperature = sensors.get_temperature()
        humidity = sensors.get_humidity()
        
        print("Temp: ", temperature) #centigrade
        print("Humidity: ", humidity) #percentage
        
        light = sensors.get_light() #1: Dark; 0:light
        print("Light: ", light)
        
        sound = sensors.get_sound() # beat count between calls
        print("Sound: ", sound)
        
        vibration = sensors.get_vibration() # beat count between calls
        print("Vibration: ", vibration)
        
        motion = sensors.get_motion()
        print("Motion: ", motion)
        
        flame = sensors.get_flame()
        print("Flame: ", flame)
        
        lpg = sensors.get_lpg()
        print("LPG: ", lpg)
        
        co = sensors.get_co()
        print("CO: ", co)
        
        smoke = sensors.get_smoke()
        print("Smoke: ", smoke)
        
        time.sleep(reading_interval)
    
def foo():
    print("test function")
    
    import requests
    userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
    resp = requests.post('http://localhost/data_collection/index.php', params=userdata)

# run the main funtion
if __name__ == "__main__":
    main()
#    foo()
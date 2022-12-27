from machine import ADC
import utime
import collections
import urequest1
import urequests
import netman
import time
import ujson
from machine import Pin
import gc

def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num


from umqttsimple import MQTTClient
from time import sleep
'''
sound_sensor = Pin(27, Pin.IN)
conversion_factor = 3.3/(4096)
clap_count = 1

while True:
    print(sound_sensor.value())
    sleep(0.1)
    sound_sensor.value(0)
    
 
    if sound_sensor.value()==1 and clap_count==1:
        sound_sensor.value(0)
        clap_count = 2
        print("ada1")
        sleep(0.1)
    if sound_sensor.value()==1 and clap_count==2:
        clap_count = 3
        sound_sensor.value(0)
        print("ada2")
        sleep(0.1)
    if sound_sensor.value()==1 and clap_count==3:
        clap_count = 1
        sound_sensor.value(0)
        sleep(0.1)
        print("ada3")
    '''

analog_value = ADC(27)
conversion_factor = 3.3/(4096)
while True:
    reading = analog_value.read_u16()
    x = clamp(reading,5000,30000)
    #print(x)
    if(x >= 30000):
        print("A")
    #print(reading)
    time.sleep(0.05)
    # utime.sleep(0.001)
    


        



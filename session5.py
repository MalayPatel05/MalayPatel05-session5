# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:55:57 2020

@author: Malay
"""
import time
import math
from io import StringIO
import sys

def time_it(fn, *args, repetitions= 1, **kwargs):
    if repetitions <1:
        raise InputError("repetitions should be > 1")    
    start_time = time.perf_counter()
    for i in range(1,repetitions+1):    
        returnval=fn(*args,**kwargs)
    end_time = time.perf_counter()
    if "UnitTest" in kwargs:
        return returnval
    else:
        return f'Executed in {round((end_time-start_time)/repetitions,6)} s'

def squared_power_list(base,exp_strt=1,exp_end=1,**kwargs):
    if base < 0:
        raise ValueError("This function is not impemented for negative numbers")
    if exp_strt <0:
        raise ValueError("This function is not impemented for negative powers")
    if exp_strt > exp_end:
        raise ValueError("exp_strt cannot be less than exp_end")

    sqared_power=[] 
    for exp in range(exp_strt,exp_end+1):
        sqared_power.append(pow(base,exp))
    return sqared_power

def polygon_area(length,sides,**kwargs):
    if type(length) not in [int,float]:
        raise TypeError("length should be integer or float value")
    if type(sides) != int:
        raise TypeError("sides should be integer value")
    if length<=0:
        raise ValueError("length should be > 0")
    if sides<3 or sides>6:
        raise ValueError("sides should be > 2 and < 6")
    if sides == 3:
        return (math.sqrt(3)*length*length/4)
    elif sides == 4:
        return (length*length)
    elif sides == 5:
        return((length*length*math.sqrt(5*(5+2*math.sqrt(5))))/4)
    elif sides == 6:
        return ((length*length*3*math.sqrt(3))/2)

def temp_converter(temp,scale,**kwargs):
    if type(temp) not in [int,float]:
        raise TypeError("Temperature should be integer or float value.")
    if scale == 'F' or scale == 'f':
        return ((temp-32)*5/9)
    elif scale == 'c' or scale == 'C':
        return ((temp*9/5)+32)
    else:
        raise TypeError(f'{scale} is not valid input for scale. Scale can be F,f,C or c.')

def speed_converter(speed,dist,time,**kwargs):
    if (type(speed) not in [int,float]) or (speed < 0):
        raise   ValueError("Speed should be positive integer or float value.")
    if dist == 'km':
        speed_converted = speed
    elif dist == 'm':
        speed_converted = speed*1000
    elif dist == 'ft':
        speed_converted = speed*3280.4
    elif dist == 'yrd':
        speed_converted = speed*1093.61
    elif dist == 'miles':
        speed_converted = speed/1.609
    else:
        raise ValueError("Distance can be only converted to km/m/ft/yrd")

    if time == 'hr':
        return speed_converted
    elif time == 'day':
        return speed_converted/24
    elif time == 'min':
        return speed_converted/60
    elif time == 's':
        return speed_converted/3600
    elif time == 'ms':
        return speed_converted/3600000
    else:
        raise ValueError("Time can be only converted to hr/day/min/s/ms")
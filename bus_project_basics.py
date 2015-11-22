# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:40:59 2015

@author: maxg
"""


import matplotlib.pyplot as plt
import random
import pandas
import string
#load shapes data
#shapes_array = numpy.loadtxt('desktop/shapes.txt',skiprows=1,delimiter=',')
path_to_files = '../Metropolitan_Travel_Data/metropolitan-atlanta-rapid-transit-authority_20151004_0136/'
routes = 'routes.txt'
shapes = 'shapes.txt'
stop_times = 'stop_times.txt'
stops = 'stops.txt'
trips = 'trips.txt'
#routes data_frame

def fill_in_transfers(ID,time_series_transfers):
    if time_series_transfers[ID] > 1:
        return 1
    return 0

def get_seconds(time_string,current_time):
    time_array= string.split(time_string,':')
    return int(time_array[0])*3600 + int(time_array[1])*60 + int(time_array[2]) - current_time 

    
stop_dictionary = {}

#shape_array = numpy.loadtxt(path_to_files+shapes,skiprows=1,delimiter=',')
routes = pandas.read_csv(path_to_files+routes)
shapes = pandas.read_csv(path_to_files+shapes)
stop_times = pandas.read_csv(path_to_files+stop_times)
stops = pandas.read_csv(path_to_files+stops)
trips = pandas.read_csv(path_to_files+trips)

#trim the fat
routes =routes[['route_id','route_color']]
stop_times = stop_times[['trip_id','arrival_time','stop_id','stop_sequence']]
stops = stops[['stop_id','stop_lat','stop_lon']]
trips = trips[['route_id','trip_id','direction_id','shape_id']]


#find transfer points
stops_and_routes = pandas.merge(stop_times,trips,on='trip_id',how='inner')
time_series_transfers = stops_and_routes.groupby('stop_id').route_id.nunique()
stop_times['is_transfer']=stop_times['stop_id'].apply(fill_in_transfers,args=(time_series_transfers,))

#convert times arrival times to seconds and subtract the current time

current_time = 36000
stop_times['arrival_secs']=stop_times['arrival_time'].apply(get_seconds,args=(current_time,))
#find specific stop 
test_stop_id = 908476
first_stop = stop_times[(stop_times.stop_id == test_stop_id) & (stop_times.arrival_secs>0) ]

# get route id's as opposed to trip_id's
routes_from_stop = pandas.merge(first_stop,trips, on='trip_id',how='inner')


#trim the fat again
#routes_from_stop = routes_from_stop[['stop_sequence','arrival_secs','route_id','direction_id']]


#group object by routes and direction and get keys:
routes_and_direction = routes_from_stop.groupby(['route_id','direction_id'])

next_stop_time = routes_from_stop.arrival_secs.order().values[0]

current_trip = routes_from_stop[routes_from_stop.arrival_secs == next_stop_time]
trip_id =  current_trip.trip_id.values[0]

stops_on_trips = stop_times[(stop_times.trip_id == trip_id) & (stop_times.arrival_secs >= next_stop_time)]

stops_on_trips

#construct data_fram all infor i need given a a specific time 

#find all routes that leave from stop in any direction

#map times for each stop from original departure

#recrusively build tree from here




#map stops function

#return interger second value given string of form hours:minutes:seconds eg 12:56:11

    
def get_seconds(time_string):
    time_array= string.split(time_string,':')
    return int(time_array[0])*3600 + int(time_array[1])*60 + int(time_array[2])

def copy_array(array,val):
    myarray=[]
    
    for item in array:
        myarray.append(item[val])
        
    return myarray
    
def findmax(array):
    max_elem = 0
    for item in array:
        if item>max_elem:
            max_elem = item
    return max_elem
    
    
def multi_plot(array):
    
    max_array_val = len(array)
    i=0
    
    while(i<max_array_val):
        array_x = []
        array_y = []
    
        while(array[i][0]==array[i+1][0]):
            array_x.append(array[i][1])
            array_y.append(array[i][2])
            if(i+2==max_array_val):
                break
            i+=1
        color_a=random.uniform(0,1)
        color_b=random.uniform(0,1)
        color_c=random.uniform(0,1)
        plt.plot(array_x,array_y,color=(color_a,color_b,color_c))
        if(i+2==max_array_val):
            break
        i+=1
    plt.show()
                


# -*- coding: utf-8 -*-
"""
@author: maxg
"""

import matplotlib as plt
import random
import pandas
import string
import numpy as np

path_to_files = '../Metropolitan_Travel_Data/metropolitan-atlanta-rapid-transit-authority_20151004_0136/'
routes = 'routes.txt'
shapes = 'shapes.txt'
stop_times = 'stop_times.txt'
stops = 'stops.txt'
trips = 'trips.txt'

routes = pandas.read_csv(path_to_files+routes)
shapes = pandas.read_csv(path_to_files+shapes)
stop_times = pandas.read_csv(path_to_files+stop_times)
stops = pandas.read_csv(path_to_files+stops)
trips = pandas.read_csv(path_to_files+trips)

routes =routes[['route_id','route_color']]
stop_times = stop_times[['trip_id','arrival_time','stop_id','stop_sequence']]
stops = stops[['stop_id','stop_lat','stop_lon']]
trips = trips[['route_id','trip_id','direction_id','shape_id']]




#functions

def fill_in_transfers(ID,time_series_transfers):
	if time_series_transfers[ID] > 1:
		return time_series_transfers[ID]
	else:
		return 0

def get_seconds(time_string, current_time = 0):
    time_array= string.split(time_string,':')
    return int(time_array[0])*3600 + int(time_array[1])*60 + int(time_array[2]) - current_time 

#find better stop times

stop_times["secs_from_start"] = stop_times['arrival_time'].apply(get_seconds)
stop_times_grouped = stop_times.groupby('trip_id')
stop_times['secs_from_zero']=stop_times_grouped['secs_from_start'].transform(lambda x: x-min(x))


#def time_between_transfers
#find transfer points

stops_and_routes = pandas.merge(stop_times,trips,on='trip_id',how='inner')
time_series_transfers = stops_and_routes.groupby('stop_id').route_id.nunique()
stop_times['is_transfer']=stop_times['stop_id'].apply(fill_in_transfers,args=(time_series_transfers,))

only_transfers = stop_times[stop_times.is_transfer > 0]

#find the unique routes
only_transfers = pandas.merge(only_transfers,trips,on='trip_id',how='inner')
time_series_transfer_routes = only_transfers.groupby('stop_id').route_id.unique()

#build adjacency chart 
# stop_id_id_adjacency[stop_id ]  =    stop_id_dictionary[stop_id] : [route,, route] -> time 

stop_id_adjacency = {}
key_list = time_series_transfer_routes.keys()

#ugly method to create dictionary i need
for key in key_list:
	stop_id_adjacency[key] = {}
	route_array = time_series_transfer_routes.pop(key)
	new_key_list = time_series_transfer_routes.keys()
	for route in route_array:
		for new_key in new_key_list:
			if time_series_transfer_routes[new_key].__contains__(route):
				if new_key in stop_id_adjacency[key]:
					stop_id_adjacency[key][new_key].append(route)
				else:
					stop_id_adjacency[key][new_key] = [route]



#useful numbers:
#		stopid1 = 904615 -> keys of stop ids -> routes 





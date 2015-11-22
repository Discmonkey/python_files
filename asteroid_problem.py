# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:44:15 2015

@author: maxg
"""

class Complex:
    
    myarray = []
    
    #shared amongst all instances of the class Complex
    
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        self.tricks = []
        #only used for each instance of the class complex
        
    def f(self,name):
        self.tricks.append(name)
        return "hello world"
        
#variables
IDEAL_MASS
DENSITY
TOTAL_CREATED
PERCENT_LOST = .00001


class Asteroid:
    totalNum = 0 
    aster_array = []
    
    
    def __init__(self,radius,theta,temp):
        self.r = radius
        self.th = theta
        self.totalNum +=1
        self.mass = 1
        self.sRadius = 1
        
    def __del__(self):
        aster_array.remove(self)
        


def find_energy(rock1,rock2):
        
    

def find_radius(rock1,rock2):
    new_mass = (rock1.mass + rock2.mass)*(1-percent)
    
    
    
        
        
        
    
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:36:38 2015

@author: maxg
"""

class package: 
    
    def __init__(self, length, width, height, price, type_box):
        self.length=length
        self.width=width
        self.height=height
        self.price=price
        self.type = type_box
        if type_box != 'wrap':        
           if(height>width or width>length):
              print 'Please initiallize package(length,width, height) \n such that length>width>height'
              raise ValueError
    def __del__(self):
        print '__del__ ... I guess you don\'t need a box of shape', self.type
        
    def volume(self):
        if(self.type != 'wrap'):
            return self.length*self.width*self.height
            
    def area(self):
        if(self.type != 'wrap'):
            return self.length*self.width
            
class shape:
    
    def __init__(self,array_bottom):
        self.bottom=array_bottom
    
    def area(self):
        
    
            
class item:
    def __init__(self,):
        
        
def generate_shape(function_array)
            
    
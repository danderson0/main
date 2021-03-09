# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:22:23 2016

@author: Tom
"""

def rising(v0,g=9.8):
    #returns height and time to height for a projectile in 1D
    h = v0**2/(2*g)
    t = v0/g
    return h,t

def falling(h,v0=0,t=0):
    # returns the time and velocity of an object falling from h and at velocity v0
    from math import sqrt
    g=9.8
    time = -v0/g + sqrt(v0**2/g**2+2*h/g)
    velo = sqrt(v0**2+2*g*h)
    return time,velo

height,time = rising(100)
tottime,velocity = falling(height,0,time)
print([tottime,height,velocity])
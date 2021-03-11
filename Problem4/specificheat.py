# -*- coding: utf-8 -*-
"""
Spyder Editor

Script to draw coefficients for a specific heat calculation
"""
import numpy as np

def specific_heat(T,gas):
    HEATS = "HeatCapCoef.txt"
    gases = np.loadtxt(HEATS, dtype={'names':   ('gas','a','b','c','d'),'formats': ('S4', 'f8','f8','f8','f8')})
    gaslist=[]
    gs = gases.tolist()
    for k in range(len(gs)):
        gaslist.append(gs[k][0].decode('UTF-8'))
    ind = gaslist.index(gas)
    sph = gases[ind]['a'] + gases[ind]['b']*T
    return sph

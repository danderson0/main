# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script written to import the data from globaltemps.txt. It assumes the file has 2 columns: year and the average temp
"""
import numpy as np

HEATS = "HeatCapCoef.txt"
gases = np.loadtxt(HEATS, dtype={'names': ('gas','a','b','c','d'),'formats': ('S4', 'f8','f8','f8','f8')})


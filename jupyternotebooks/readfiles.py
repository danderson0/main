# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script written to import the data from globaltemps.txt. It assumes the file has 2 columns: year and the average temp
"""

TEMPS = "data//globaltemps.txt"
infile = open(TEMPS, "r")
year = []
temps = []
for line in infile: 
    info = line.split()
    year.append(info[0])
    temps.append(info[1])

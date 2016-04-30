#!/bin/python

import sys


time = raw_input().strip()

#print time[8:10]

if time[8:10]=='AM':
    if time[0:2]=='12':
        time= '00' + time[2:8]
    else:
        time=time[0:8]
    

if time[8:10]=='PM':
    if time[0:2]=='12':
        time=time[0:8]
    else:
        m=int(time[0:2]) + 12
        time= str(m) + time[2:8]
print time[0:8]

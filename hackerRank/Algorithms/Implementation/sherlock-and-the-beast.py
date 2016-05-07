#!/bin/python

t=int(raw_input().strip())

for i in range(t):
    n=int(raw_input().strip())
    j=0 # number of 5's
    f=''
    if n%3==0:
        j=n
        for p in range(j):
            f=f + '5'
        final=int(f)
    if n%3==1:
        if n<10:
            final=-1
        else:
            j=n-10
            for p in range(j):
                f=f + '5'
            final=int(f+'3333333333')            
    if n%3==2:
        if n<5:
            final=-1
        else:
            j=n-5
            for p in range(j):
                f=f + '5'
            final=int(f+'33333')
    print final
    
    

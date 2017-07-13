'''
Alcohol consumption exercise from dataquest.io 
'''
import csv
import numpy

f = open("world_alcohol.csv", 'r')
world_alcohol = list(csv.reader(f))
world_alcohol=numpy.genfromtxt("world_alcohol.csv",delimiter=",")

world_alcohol=numpy.genfromtxt("world_alcohol.csv",delimiter=",",dtype= "U75" , skip_header =True)
print(world_alcohol )





totals = {}
#year =world_alcohol[:,0]=='1989'

countries = world_alcohol[:,2]
print countries


for row in countries:
    country_consumption=(world_alcohol[:,0]=='1989') & (world_alcohol[:,2] ==row)
    f=(world_alcohol[country_consumption,4]=='')
    world_alcohol[f,4]='0'
    new=world_alcohol[country_consumption,4]
    new=new.astype(float)
    total=new.sum()
    totals[row]=total



highest_value = 0
highest_key = None
for key in totals:
    new = totals[key]
    if (highest_value < new ):
        highest_value=new
        highest_key = key

print 'Highest alcohol consumption'
print (highest_key)
print (highest_value)


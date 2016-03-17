#!/usr/bin/python
f= open("dq_unisex_names.csv", "r")
data = f.read ()
data_list=data.split("\n")
print(data_list[0:5]) 

string_data=[]
for row1 in data_list:
    comma_list=row1.split(",")
    string_data.append(comma_list)
    
print(string_data[0:5])

numerical_data =[]
for row2 in string_data:
    new=[row2[0],float(row2[1])]
    numerical_data.append(new)
print(numerical_data[0:5])

numerical_data[len(numerical_data)-1]

thousand_or_greater =[]
for row3 in numerical_data:
    if (row3[1] >= 1000):
        thousand_or_greater.append(row[0])
print(thousand_or_greater[0:10])

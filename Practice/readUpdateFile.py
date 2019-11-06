#Program to convert fixed width file to csv files.
testtxt = open('./test.txt', 'r')
testlist = testtxt.readlines()
testtxt.close()
dict_ = {}

name = ros_version

if '_' in name:
    name_list = name.split(str="_", 1))
for item in testlist:
 RECORDTYPE = item[0:3]
 
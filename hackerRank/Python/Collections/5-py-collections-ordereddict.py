'''
https://www.hackerrank.com/challenges/py-collections-ordereddict
'''


from collections import OrderedDict
import re

a=int(raw_input())
ordered_dictionary = OrderedDict()
for i in range(a):
    string=raw_input()
    price= [int(s) for s in string.split() if s.isdigit()][0]
    item_name = " ".join(re.findall("[a-zA-Z]+", string))
    if item_name in ordered_dictionary.keys():
        ordered_dictionary[item_name]= ordered_dictionary[item_name] + price
    else:
        ordered_dictionary[item_name]=price

for j in ordered_dictionary.keys():
    print (j+' '+str(ordered_dictionary[j]))

'''
https://www.hackerrank.com/challenges/word-order
'''

from collections import OrderedDict
a=int(raw_input())

ordered_dictionary = OrderedDict()
for i in range(a):
    string =raw_input()
    if string in ordered_dictionary.keys():
        ordered_dictionary[string]= ordered_dictionary[string] + 1
    else:
        ordered_dictionary[string]=1
print len(ordered_dictionary)
print ' '.join(map(str,ordered_dictionary.values()))

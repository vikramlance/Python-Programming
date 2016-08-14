'''
https://www.hackerrank.com/challenges/word-order
'''

from collections import Counter

n = int(raw_input())
words = [raw_input().strip() for _ in range(n)]
counts = Counter(words)

print len(counts)

for word in words:
    k = counts.pop(word, None)
    if k == None:
        continue
    else:
        print k, # comma stops print from ending with newline

'''
# Inefficient method
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
'''

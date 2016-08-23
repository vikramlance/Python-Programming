'''
https://www.hackerrank.com/challenges/most-commons
'''
import collections
a= list(raw_input())
d=collections.Counter(a)


if len(set(d.values()))==1:
    for i in sorted(d.most_common(3)):
        print (i[0]+' '+str(i[1]))

if len(set(d.values()))!=1:
    for i in (d.most_common(3)):
        print (i[0]+' '+str(i[1]))

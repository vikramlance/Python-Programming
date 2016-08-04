import collections
a=raw_input().strip()
b=list(raw_input().split())
#c=set(b)
d=collections.Counter(b)

for i in d.keys():
    if d[i]==1:
        print i
        break

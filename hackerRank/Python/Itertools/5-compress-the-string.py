from itertools import groupby
data=list(raw_input())

m = []

for k, g in groupby(data):
    m.append( str((len(list(g)), int(k))))
print ' '.join(map(str,m))

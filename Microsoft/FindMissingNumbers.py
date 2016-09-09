
from itertools import imap, chain
from operator import sub


n=int(raw_input())

for i in range(n):
    a=map(int, (raw_input().split()))
    a=sorted(a)

    m= list(chain.from_iterable((a[j] + d for d in xrange(1, diff))
                        for j, diff in enumerate(imap(sub, a[1:], a))
                        if diff > 1))
    print ' '.join(str(x) for x in m)

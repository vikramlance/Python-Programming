'''
itertools.product()

https://www.hackerrank.com/challenges/itertools-product
'''


from itertools import product
    
a=map(int,raw_input().split())
b=map(int,raw_input().split())


print (" ".join( repr(e) for e in list(product(a,b))))

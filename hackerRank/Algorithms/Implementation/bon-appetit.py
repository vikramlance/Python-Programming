'''
https://www.hackerrank.com/challenges/bon-appetit
'''
n,k=raw_input().split()
n=int(n)
k=int(k)

a=map(int, raw_input().split())
b=int(raw_input()) 

if (2*b== (sum(a) - a[k])):
    print "Bon Appetit"
else:
    print ( b - ((sum(a) - a[k])//2))

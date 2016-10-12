'''
https://www.hackerrank.com/challenges/reverse-game
'''

t=int(raw_input())

for i in range(t):
    index=0
    n,k=(raw_input().split())
    n=int(n)
    k=int(k)
    if(k<n/2):
        index=2*k+1
    else:
        index=2*(n-1-k)
    print index 

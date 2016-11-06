'''
https://www.hackerrank.com/challenges/alternating-characters
'''


a= int(raw_input())

for i in range(a):
    b=raw_input()
    k=0
    newb=''
    oldb=''
    for j in b:
        newb=j
        if newb==oldb:
            k+=1
        oldb= newb
    print k

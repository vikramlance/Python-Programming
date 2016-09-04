'''
https://www.hackerrank.com/challenges/exceptions
'''

n= int(input())

for i in range(n):
    a,b=input().split()

    try:
        print (int(a)//int(b))
    except ZeroDivisionError as e:
    	print ("Error Code:",e)
    except ValueError as er:
    	print ("Error Code:",er)

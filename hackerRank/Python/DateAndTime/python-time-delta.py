'''
https://www.hackerrank.com/challenges/python-time-delta
'''


from datetime import datetime
n=int(input())

k = "%a %d %b %Y %H:%M:%S %z"
for i in range(n) :
    a = datetime.strptime(input(), k)
    b = datetime.strptime(input(), k)
    print(abs(int((a-b).total_seconds())))

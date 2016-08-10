'''
https://www.hackerrank.com/challenges/py-collections-namedtuple
'''



n= int(raw_input())
sum=0
a=list(raw_input().split()).index("MARKS")
for i in range(n):
    sum = sum + int(list(raw_input().split())[a])
print "%.2f" %(float(sum)/float(n))

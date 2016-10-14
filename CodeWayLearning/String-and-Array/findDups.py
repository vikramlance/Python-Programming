'''
ans to question 1
'''


a= [9,1,5,3,7,9,2,10,4,8,6]



import collections

counter=collections.Counter(a)

m= (counter.most_common(1))

j= ''.join(map(str, m))

print list(j)[1]

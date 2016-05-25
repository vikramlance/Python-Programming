import __builtin__

N = int(raw_input())
T = tuple(map(int, raw_input().split()))

print hash(T)


'''
T = raw_input()
#print T
k=T.replace(" ", "")
m=tuple(k)
print (hash(m))
l=(1,2)

m = tuple(int(x.strip()) for x in raw_input().split(' '))
print hash(m)

'''

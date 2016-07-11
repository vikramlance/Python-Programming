
k=raw_input()
a=set(map (int, (raw_input().split(' '))))
b=0

for i in a:
	b=i+b

c= float (b) / float(len(a))

print c

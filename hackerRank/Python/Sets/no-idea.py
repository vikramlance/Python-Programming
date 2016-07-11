p=raw_input()
q=map (int, (raw_input().strip().split(' ')))



a=set(map (int, (raw_input().strip().split(' '))))
b=set(map (int, (raw_input().strip().split(' '))))


s=0
for i in q:
	if i in a:
		s=s+1
	if i in b:
		s=s-1

print s

n = input()
s = set(map(int, raw_input().split())) 
N= int(raw_input())
for i in range (N):
	k=raw_input().split()
	if k[0]=='pop':
		s.pop()
	if k[0]=='remove':
		s.remove(int(k[1]))
		
	if k[0]=='discard':
		s.discard(int(k[1]))

print sum(s)

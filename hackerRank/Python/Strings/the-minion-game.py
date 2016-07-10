

a=list(raw_input())
s=0
r=0
p=[]
q=[]
for i in range(len(a)):
	if (a[i] in 'AEIOU'):
		p.append(i)
	else:
		q.append(i)

for i in p:
	r=r+ len(a) - i
for i in q:
	s=s+len(a) - i

if s>r:
	print ("Stuart %i") %(s)
elif s<r:
	print ("Kevin %i") %(r)
else:
	print 'Draw'


'''
inefficient solution 
a=list(raw_input())
s=0
r=0
for i in range(1,len(a)+1):
	for k in range(len(a)-i+1):
		if (a[k] in 'AEIOU') :
			r=r+1
		else:
			s=s+1				
if s>r:
	print ("Stuart %i") %(s)
elif s<r:
	print ("Kevin %i") %(r)
else:
	print 'Draw'
'''	

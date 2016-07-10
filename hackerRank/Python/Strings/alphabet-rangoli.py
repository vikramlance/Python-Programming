a=int(raw_input())
for i in xrange(-a,a+1):
	#b=''
	m=''
	i= abs(i)
	if i != 1:
		#print i
		if i==0:
			i=1
		for k in range(i,a+1):
			c=chr(96 + i)
			if k!=i:
				#b=b+chr(96 + k)+'-'
				m=m+'-'+chr(96 + k)
		b=m[::-1]
		
		print 2*(i-1)*'-'+b+c+m+2*(i-1)*'-'

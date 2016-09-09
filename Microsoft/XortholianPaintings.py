a=raw_input().split()
b=[]
c={'orange':'red', 'orange':'yellow', 'green':'yellow', 'green':'blue', 'purple':'blue', 'purple':'red'}
for i in (range(len(a))):
	if (i==0 or i==(len(a)-1)):
		b.append(a[i])
	else:
		if a[i]==a[i-1]:
			b.append('blank')
		else:
			if a[i]==''

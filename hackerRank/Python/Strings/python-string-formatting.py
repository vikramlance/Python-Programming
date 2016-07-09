a= int(raw_input())

'''
for i in range(a+1):
	x=str(i)
	y=str(oct(i))
	z=str(hex(i))
	w=str(bin(i))
	print x+' '+ y+' '+ z+' '+ w
	#print (i + oct(i) + hex(i) + bin(i)) 
	
'''


for i in range(1,a+1):
	x=str(i)
	y=str(format(i, 'o'))
	z=str(format(i, 'X'))
	w=str(format(i, 'b'))
	print x.rjust(len(str(format(a, 'b'))))+' '+y.rjust(len(str(format(a, 'b'))))+' '+z.rjust(len(str(format(a, 'b'))))+' '+w.rjust(len(str(format(a, 'b'))))
	#+' '+ y+' '+ z+' '+ w

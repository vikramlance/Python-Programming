'''
Given a string, print all the unique characters in the string in reverse order. Take input from the prompt screen and write output to a text file.
	Ex: given: abbccccccdddddddeeeaaaaa
		output: aedcba
    
'''


a='abbccccccdddddddeeeaaaaa'
k=[]
old=''
for i in list(a):
	new=i
	if new==old:
		continue
	else:
		k.append(new)
		old=new
	#	print old
print ''.join(k)[::-1]

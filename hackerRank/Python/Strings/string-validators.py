a= list (raw_input())

for i in a:
	k='False'
	if i.isalnum():
		k= 'True'
		break
print k

for i in a:
	k='False'
	if i.isalpha():
		k= 'True'
		break
print k	

for i in a:
	k='False'
	if i.isdigit():
		k= 'True'
		break
print k	

for i in a:
	k='False'
	if i.islower():
		k= 'True'
		break
print k	

for i in a:
	k='False'
	if i.isupper():
		k= 'True'
		break
print k	

'''
check if string has all unique characters
'''

a="abdnscf"
chars = list(a)


if len(chars) == len(set(chars)):
	print "unique"
else:
	print "not unique"

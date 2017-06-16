'''
check if string has all unique characters and print if it is unique or not unique.
'''

a="abdnscf"
chars = list(a)


if len(chars) == len(set(chars)):
	print "unique"
else:
	print "not unique"

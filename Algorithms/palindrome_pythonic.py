'''
find out if given string is palindrome or not.
'''
n=raw_input()
#pythonic way to slice ans reverse the string
if str(n) == str(n)[::-1]:
    print "Palindrome"
else:
    print "not palindrome"  

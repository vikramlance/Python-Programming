'''
Find if given string is palindrome or not.
'''

a=raw_input()
n=len(a)
# use stack for checking if given string is palindrome

stack=list(a)
print stack
for i in range(n/2):
    m=i
    k=stack.pop()
    if stack[i]!=k:
    	break

print m
if (m+1)==n/2:
    print "Palindrome"
else:
    print "not palindrome"   

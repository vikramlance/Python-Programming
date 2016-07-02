a= raw_input()
b=""
for letter in a:
    #print letter
    if letter.islower():
    	b=b+letter.upper()
    else:
    	b= b+letter.lower()
print b

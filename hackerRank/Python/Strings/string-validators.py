
a=raw_input()

if a.isalnum():
    print "True"
else:
    print "False"

if a.isalnum() and not a.isdigit():
    print "True"
else:
    print "False"

if a.isalnum() and not a.isalpha():
    print "True"
else:
    print "False"

if (a.isalnum() and not (a.islower() and a.isupper() )) or (a.isalnum() and not (a.islower() and a.isupper() )) :
    print "True"
else:
    print "False"

if a.isupper():
    print "True"
else:
    print "False"

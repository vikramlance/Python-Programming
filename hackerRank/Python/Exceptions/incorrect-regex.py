import re
n=int(input())

for i in range (n):
    a= input()
    try:
        re.compile(a)
        is_valid = True
    except re.error:
        is_valid = False
    print (is_valid)

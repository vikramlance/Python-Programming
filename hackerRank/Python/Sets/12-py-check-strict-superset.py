A = set(input().split()) 
a = int(input());

for i in range(a):
    B = set(input().split())
    if A>B:
        result=True
    else:
        result=False
        break
print (result)

a= int(raw_input())

for i in range(a):
    b= raw_input().split()
    for k in range(len(b)):
        if (k ==0):
            m=set(b[k])
        else:
            m=(m & set(b[k]))
    print ''.join(map(str,sorted(m)))

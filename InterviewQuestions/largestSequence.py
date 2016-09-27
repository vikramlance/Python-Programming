a=[45,4,1,5,6,7,2,8,23,43]

b=sorted(a)
print b
m=[]
p=[]
for i in range(len(b)):
    if i==0:
        m.append(b[0])
        p=m
    else:
        if b[i] - b[i-1] ==1:
            p.append(b[i])

        else:
            if len(m) < len(p):
                m=p
            p=[]

print m

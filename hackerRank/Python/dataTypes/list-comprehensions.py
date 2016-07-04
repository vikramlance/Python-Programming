x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
n=int(raw_input())
print x,y,z,n
m=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k)!=n:
                m.append([i,j,k])
print m

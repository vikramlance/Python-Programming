

a=5
b=56
if b>a:
    temp=a
    a=b
    b=temp


def gcd(a,b):
    if a==b:
        print "hi"
        return a
    if a>b:
        print "hi bi"
        print a
        print b
        gcd(a-b,b)

    else:
        if b%a==0:
            print "hi m"
            return a
        else:
            return 1

k= gcd(a,b)
print k

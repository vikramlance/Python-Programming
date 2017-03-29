'''
Find GCD of two given numbers

Given numbers 21 and 56 for example
'''
a=21
b=56

def gcd(a,b):
    if a>=b:
        if (a%b==0) or (b==1):
            print b
        else:
            gcd(a-b,b)
    else:
        if (b%a==0) or (a==1):
            print a
        else:
            gcd(b-a,a)

gcd(a,b)

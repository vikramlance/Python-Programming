'''
Find GCD of two given numbers (can be extended to n numbers by just finding GD of 2 numbers at a time )

Given numbers 21 and 56 for example
'''
a=21
b=56

def gcd(a,b):
    if a>=b:
        if (a%b==0) or (b==1):
            print b
        else:
            gcd(a-b,b) # apply the property of gcd
    else:
        if (b%a==0) or (a==1):
            print a
        else:
            gcd(b-a,a)

gcd(a,b)

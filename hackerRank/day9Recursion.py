N=int(raw_input().strip())

def factorial(m):
    a=0
    
    for i in (m,0,-1):
        if m<=1:
            a=1
        else:
            a=m*factorial(m-1)
    return a
print factorial(N)

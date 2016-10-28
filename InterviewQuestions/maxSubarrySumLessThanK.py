

a= [3,1,2,1]

n= len(a)
k= 4

def  maxLength(a, k):
    
    counter, i, r = 0, 0, float('-inf')
    for j in range(len(a)):
        counter += a[j]
        while i <= j and counter > k:
            counter -= a[i]
            i += 1
        if counter <= k:
            r = max(r, j - i + 1)
    return r if r > float('-inf') else None
    
    
print maxLength([3,1,2,1], 4)

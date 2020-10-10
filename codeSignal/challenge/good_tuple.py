"""

"""

def goodTuples(a):
    count = 0
    for i in range(len(a)-2):
        if ( a[i] == a[i+1] and a[i] != a[i+2] ) or (a[i] != a[i+1] and a[i] == a[i+2] ) or (a[i] != a[i+1] and a[i+1] == a[i+2] ):
            count += 1
            
    return count
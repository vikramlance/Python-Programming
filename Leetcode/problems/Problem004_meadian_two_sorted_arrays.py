"""Find the median of all the numbers given in two different sorted arrays

a = [1,3]
b= [2]

output: 2

Input:
a = [1,2]
b = [3,4] 

Output: 2.5

"""

def brute_force_median(a, b):
    a.extend(b)

    print(a, b)
    sorted(a)

    print(median(a))

def median(c):
    size = len(c)
    if size % 2 == 0:
        print(c[(size - 1) / 2])
        print(c[size / 2])
        median = (c[size / 2] + c[(size - 1) / 2]) / 2
        print((c[size / 2] + c[(size - 1) / 2]))
        print(5/2)
    else:
        median = (c[size / 2])

    return median

a = [1,2]
b = [3,4] 


brute_force_median(a, b)


"""
Given an array, arrange it in an zig-zag manner.
For Example –

Input : 9, 6, 3, 4, 10, 12, 5

Output : 6, 3, 9, 4, 10, 5, 12

"""
array = [9, 6, 3, 4, 10, 12, 5]

array.sort()

new_array = []

array_len = len(array)

print((array_len - 1) / 2)
print(array[0: (array_len - 1) / 2])
print(array[((array_len - 1) / 2): (array_len)])

n =0
for i in array[0: (array_len - 1) / 2]:
    for j in array[((array_len - 1) / 2): (array_len)]:
        if n%2 == 0:
            print (i)
        else:
            print(j)

        n = n +1
        continue
        



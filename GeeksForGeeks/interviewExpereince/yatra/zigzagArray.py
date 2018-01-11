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

new_array_first = array[0: (array_len - 1) / 2]
new_array_last = array[((array_len - 1) / 2): (array_len)]
n = 0
for i in xrange(len(new_array_first)):
    new_array_last.insert((2 * i + 1), new_array_first[i])

print(new_array_last)

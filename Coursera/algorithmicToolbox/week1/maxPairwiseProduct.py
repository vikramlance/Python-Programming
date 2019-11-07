input1 = 10
input2 = [2, 4, 5, 11, 9, 5, 2, 1, 8, 6, 1]

max_num = 0
next_to_max_num = 0

for i in input2:
    if max_num < i:
        max_num = i

input2.remove(max_num)

for i in input2:
    if next_to_max_num < i:
        next_to_max_num = i

print('maximum pairwise product')
print(max_num * next_to_max_num)

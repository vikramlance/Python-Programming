
n = int(input())

arr = map(int, input().strip().split(' '))

while


for i in range(int(input())):
    arr_len = int(input())

    arr = []

    for j in range(arr_len):
        z = random.randint(1, 1000)
        arr.append(z)

    while not is_comp(arr):
        for j in range(arr_len):
            z = random.randint(1, 1000)
            arr.append(z)

    print(arr)

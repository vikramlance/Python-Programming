"""
https://codingbat.com/prob/p199484 


Array-2 > tenRun
prev  |  next  |  chance
For each multiple of 10 in the given array, change all the values following it to be that multiple of 10, until encountering another multiple of 10. So {2, 10, 3, 4, 20, 5} yields {2, 10, 10, 10, 20, 20}.


tenRun([2, 10, 3, 4, 20, 5]) → [2, 10, 10, 10, 20, 20]
tenRun([10, 1, 20, 2]) → [10, 10, 20, 20]
tenRun([10, 1, 9, 20]) → [10, 10, 10, 20]
"""

def ten_run(arr):
    last_ten = 0
    for i in range(len(arr)):
        if arr[i]%10 == 0:
            last_ten = arr[i]
        elif last_ten > 0:
            arr[i] = last_ten
    return arr

print(ten_run([2, 10, 3, 4, 20, 5]))
print(ten_run([10, 1, 20, 2]))
print(ten_run([10, 1, 9, 20]))



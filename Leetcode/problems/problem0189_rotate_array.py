"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0


-- 
using extra space

def roate(nums, k):
    len_nums = len(nums)
    
    
    for i in range(k):
        temp_nums = [None]
        print("aaaa", nums, len_nums)
        temp_nums[0] = nums[len_nums - 1 ]
        temp_nums.extend(nums[:len_nums -1]) 
        print('temp_nums', temp_nums)
        nums = []
        nums.extend(temp_nums)
        print('nums', nums)

    print(nums)

nums = [1,2,3,4,5,6,7]

k = 3

roate(nums, k)


-----
# time limit exceeded
def roate(nums, k):
    len_nums = len(nums)
    
    
    for i in range(k):
        last_num = nums[-1] 
        print(last_num)
        
        for j in range(len_nums-1, 0, -1):
            print('nums', nums)
            nums[j] = nums[j-1]

        nums[0] = last_num
        

    print(nums)

nums = [1,2,3,4,5,6,7]

k = 3

roate(nums, k)

"""

def roate(nums, k):
    len_nums = len(nums)
        
    if len_nums < k:
        k = k% len_nums
    temp_nums = nums[:len_nums -k]
    for i in range(k):
        nums[i] = nums[i+ len_nums - k]
    for j in range(len_nums -k):
        nums[j+k] = temp_nums[j]   
    

    print(nums)

nums = [-1]
# [5, 6, 7, 1, 2, 3, 4]
k = 2

# [-1,-100,3,99]
# 2

roate(nums, k)


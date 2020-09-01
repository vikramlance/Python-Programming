"""

Maximum subarry with product of all elements is positive

nums = [1,-2,-3,4] out = 4
Input: nums = [0,1,-2,-3,-4] 3
Input: nums = [-1,-2,-3,0,1] 2         
Input: nums = [-1,2] 1        
nums = [1,2,3,5,-6,4,0,10] 4
"""

# read items in nums 
# if item is postive add it to temp arr
# if len of max subarry < temp_subarr then max sub arr = temp sub arr

temp_arr = []
max_subarray = []
flag_negative = False
for i in nums:
    if i > 0:
        temp_arr.append(i)
        if len(max_subarray) < len(temp_arr):
            max_subarray = temp_arr
        
        if i == 0:
            temp_arr = []
        
        if i < 0:
            if flag_negative: 
                flag_negative = False
            else:
                flag_negative = True
            
            temp_arr.append(i)


            


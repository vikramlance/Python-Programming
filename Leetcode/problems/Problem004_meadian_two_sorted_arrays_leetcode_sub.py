"""Find the median of all the numbers given in two different sorted arrays

a = [1,3]
b= [2]

output: 2

Input:
a = [1,2]
b = [3,4] 

Output: 2.5

"""
a = [1,3]
b = [2] 
temp_array = []

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        a = nums1
        b = nums2
        temp_array = []

        while a or b:
            if a:
                a_least_num = a[0]
            if b:
                b_least_num = b[0]
            if not a and b:
                temp_array.extend(b)
                break
            if not b and a:
                temp_array.extend(a)
                break
            if a_least_num < b_least_num:
                temp_array.append(a_least_num)
                del a[0]
            elif a_least_num > b_least_num:
                temp_array.append(b_least_num)
                del b[0]
            else:
                temp_array.append(a_least_num)
                temp_array.append(b_least_num)
                del a[0]
                del b[0]

        total_nums = 0
        total_nums = len(temp_array)
        if total_nums % 2 == 0:
            return ((temp_array[total_nums // 2] + temp_array[(total_nums // 2) - 1]) / 2)
        else:
            return (temp_array[total_nums // 2] )

test_input = [{'nums1':[1, 3], 'nums2':[2]}, {'nums1':[1, 2], 'nums2':[3, 4]}]

Solution_obj = Solution()
for item in test_input:
    print(Solution_obj.findMedianSortedArrays(item['nums1'], item['nums2']))

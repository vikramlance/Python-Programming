"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""
class solution:

    def intersection(self, nums1, nums2):

        intersection_list = []
        for i in range(len(nums1)):
            if nums1[i] in intersection_list:
                continue
            for j in range(len(nums2)):
                if nums1[i] in intersection_list:
                    continue
                if nums1[i] == nums2[j]:
                    intersection_list.append(nums1[i])
                    print(i, j)
                    print(intersection_list)

                    continue
        return intersection_list

    def intersection_1(self, nums1, nums2):

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        len1 = len(nums1_set)

        len2 = len(nums2_set)

        if len1 < len2:
            smaller_set = nums1_set
            larger_set = nums2_set
        else:
            smaller_set = nums2_set
            larger_set = nums1_set

        intersection_list = []

        for i in smaller_set:
            if i in larger_set:
                intersection_list.append(i)
        return intersection_list

    def intersection_2(self, nums1, nums2):

        result = set()
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for i in nums1_set:
            if i in nums2_set:
                result.add(i)
        return list(result)

nums1 = [1, 3, 4, 8]
nums2 = [3, 4, 5, 8, 9, 2]
test = solution()

print(test.intersection_1(nums1, nums2))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
test = solution()

print(test.intersection_1(nums1, nums2))

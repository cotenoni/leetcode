from typing import List

#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_array = []

        i = j = 0
        while i < m or j < n:
            if i < m and (j >= n or nums1[i] < nums2[j]):
                sorted_array.append(nums1[i])
                i += 1
            else:
                sorted_array.append(nums2[j])
                j += 1
        
        for i, num in enumerate(sorted_array):
            nums1[i] = num



sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3) #1,2,2,3,5,6
sol.merge([1], 1, [], 0) #1
sol.merge([0], 0, [1], 1) #1
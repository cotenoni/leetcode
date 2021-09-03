from typing import List

#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m -1 
        j = n - 1
        end = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[end] = nums1[i]
                i -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
    
            end -=1
        print(nums1)




sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3) #1,2,2,3,5,6
sol.merge([5,6,7,0,0,0], 3, [1,2,3], 3) #1,2,3,5,6,7
sol.merge([5,6,7,0,0,0], 3, [1,2,7], 3) #1,2,5,6,7,7
sol.merge([1], 1, [], 0) #1
sol.merge([0], 0, [1], 1) #1
from typing import List

#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]



sol = Solution()
print(sol.findMin([3,4,5,1,2]) == 1)
print(sol.findMin([4,5,6,7,0,1,2]) == 0)
print(sol.findMin([11,13,15,17]) == 11)

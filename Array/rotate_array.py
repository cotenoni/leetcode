from typing import List

#https://leetcode.com/problems/rotate-array/
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3) #[5,6,7,1,2,3,4]
solution.rotate([-1,-100,3,99], 2) #[3,99,-1,-100]
solution.rotate([1,2], 3) #[2, 1]



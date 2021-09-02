from typing import List

#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[low] == target and nums[high] == target:
                return [low, high]
            elif nums[mid] == target:
                if nums[low] != nums[mid]:
                    low += 1
                if nums[high] != nums[mid]:
                    high -= 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
         
        return [-1, -1]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8) == [3,4])
print(sol.searchRange([5,7,7,8,10], 8) == [3,3])
print(sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1])
print(sol.searchRange([], 0) == [-1, -1])
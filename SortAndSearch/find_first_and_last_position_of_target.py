from typing import List
import bisect

#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        low = bisect.bisect_left(nums, target)
        high = bisect.bisect_right(nums, target)
    
        if low < high:
            return [low, high - 1]
         
        return [-1, -1]

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8) == [3,4])
print(sol.searchRange([5,7,7,8,10], 8) == [3,3])
print(sol.searchRange([5,7,7,8,8,10], 6) == [-1, -1])
print(sol.searchRange([], 0) == [-1, -1])
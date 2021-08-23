from typing import List

#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target_numbers = set(range(len(nums) + 1))
        return (target_numbers - set(nums)).pop()

sol = Solution()
print(sol.missingNumber([3,0,1]) == 2)
print(sol.missingNumber([0,1]) == 2)
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8)
print(sol.missingNumber([0]) == 1)
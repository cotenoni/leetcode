from typing import List

#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target_sum = n * (n + 1) // 2

        nums_sum = 0
        for num in nums:
            nums_sum += num
        
        return target_sum - nums_sum

sol = Solution()
print(sol.missingNumber([3,0,1]) == 2)
print(sol.missingNumber([0,1]) == 2)
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8)
print(sol.missingNumber([0]) == 1)
from typing import List

#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = nums[0]

        for n in range(1, len(nums)):
            max_ending_here = max(nums[n], nums[n] + max_ending_here)

            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(solution.maxSubArray([1])) # 1
print(solution.maxSubArray([5,4,-1,7,8])) # 23


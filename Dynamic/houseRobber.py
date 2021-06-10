#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        answer = [0] * len(nums)
        answer[0] = nums[0]
        answer[1] = nums[1]

        for i in range(2, len(nums)):
            firstPossibleSum = nums[i] + answer[i - 2]
            secondPossibleSum = 0
            if i - 3 >= 0:
                secondPossibleSum = nums[i] + answer[i - 3]

            answer[i] = max(firstPossibleSum, secondPossibleSum)

        return max(answer[len(nums) - 1], answer[len(nums) - 2])

       

solution = Solution()
print(solution.rob([1,2,3,1])) #4
print(solution.rob([2,7,9,3,1])) #12
print(solution.rob([2,1,1,2])) #4

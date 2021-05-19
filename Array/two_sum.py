from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer: List[int]
        hash = { nums[i] : i  for i in range(0, len(nums)) }

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in hash and hash[remaining] != i:
                answer = [i, hash[remaining]]

        answer.sort()
        return answer


solution = Solution()
solution.twoSum([2,7,11,15], 9) #expected: [0,1]
solution.twoSum([3,2,4], 6) #expected: [1,2]
solution.twoSum([3,3], 6) # expected: [0,1]
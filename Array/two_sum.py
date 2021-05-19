from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer: List[int]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j):
                    if nums[i] + nums[j] == target:
                        answer = [j, i]
        
        print(answer)
        return answer


solution = Solution()
solution.twoSum([2,7,11,15], 9) #expected: [0,1]
solution.twoSum([3,2,4], 6) #expected: [1,2]
solution.twoSum([3,3], 6) # expected: [0,1]
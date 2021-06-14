from typing import List

#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums.pop(i + 1)

            i += 1
                
        return len(nums)


solution = Solution()
nums = [1,1,2]
print(solution.removeDuplicates(nums)) #2
print(nums) #[1,2]

nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums)) #5
print(nums) #[0,1,2,3,4]

nums = [1,1]
print(solution.removeDuplicates(nums)) #1
print(nums) #[1]

nums = [1,2]
print(solution.removeDuplicates(nums)) #2
print(nums) #[1,2]

nums = []
print(solution.removeDuplicates(nums)) #0
print(nums) #[]

nums = [1]
print(solution.removeDuplicates(nums)) #1
print(nums) #[]

# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = [0] * len(nums)
        max_position = 0

        for i, num in enumerate(nums):
            if i + num > max_position:
                max_updatable_pos = min(len(jump_count), i + num + 1)
                for j in range(max_position + 1, max_updatable_pos):
                    jump_count[j] = jump_count[i] + 1
                max_position = i + num
                    
            #print(jump_count)
            if max_position >= len(nums) - 1:
                return jump_count[-1]

        return -1

sol = Solution()
print(sol.jump([0])) #0
print(sol.jump([1])) #0
print(sol.jump([2,3,1,1,4])) #2
print(sol.jump([2,3,0,1,4])) #2
print(sol.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])) #2
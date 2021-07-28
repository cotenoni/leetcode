from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_position = 0
        for i, num in enumerate(nums):
            if max_position >= len(nums) - 1:
                return True
            
            if i > max_position:
                return False
            
            max_position = max(max_position, i + num)

        return False
           

solution = Solution()
print(solution.canJump([2,3,1,1,4])) #true
print(solution.canJump([3,2,1,0,4])) #false
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        if len(nums) == 1:
            return True

        max_position = 0
        pos = 0

        while pos < len(nums):
            max_position = max(max_position, pos + nums[pos])
            pos += 1
            if max_position >= len(nums) - 1:
                return True
            if max_position < pos:
                return False
            
        return True
            

solution = Solution()
print(solution.canJump([2,3,1,1,4])) #true
print(solution.canJump([3,2,1,0,4])) #false
from typing import List

#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1

                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j = i
        

sol = Solution()
a = [0,1,0,3,12]
sol.moveZeroes(a)
print(a == [1,3,12,0,0])

a = [0, 0, 1, 3, 0, 12]
sol.moveZeroes(a)
print(a == [1, 3, 12, 0, 0, 0])

a = [0]
sol.moveZeroes(a)
print(a == [0])

a = [0, 0, 0, 0, 0]
sol.moveZeroes(a)
print(a == [0, 0, 0, 0, 0])

a = [1, 2, 3, 4, 5]
sol.moveZeroes(a)
print(a == [1, 2, 3, 4, 5])

a = [1, 2, 3, 4, 0]
sol.moveZeroes(a)
print(a == [1, 2, 3, 4, 0])
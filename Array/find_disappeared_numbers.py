from typing import List

#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        return [i + 1 for i, num in enumerate(nums) if num > 0]


sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6])
print(sol.findDisappearedNumbers([1,1]) == [2])
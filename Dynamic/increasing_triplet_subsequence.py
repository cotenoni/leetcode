from typing import List

#https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        table = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    table[i] = max(table[i], table[j] + 1)
        
        return max(table) >= 3
        


sol = Solution()
# print(sol.increasingTriplet([1,2]) == False)
print(sol.increasingTriplet([1,2,3,4,5]) == True)
print(sol.increasingTriplet([5,4,3,2,1]) == False)
print(sol.increasingTriplet([2,1,5,0,4,6]) == True)

from typing import List

#https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        i, j, k = nums[0], float("inf"), float("inf")
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                k = num
                
        return j != float("inf") and k != float("inf")
        


sol = Solution()
print(sol.increasingTriplet([1,2]) == False)
print(sol.increasingTriplet([1,2,3,4,5]) == True)
print(sol.increasingTriplet([5,4,3,2,1]) == False)
print(sol.increasingTriplet([2,1,5,0,4,6]) == True)

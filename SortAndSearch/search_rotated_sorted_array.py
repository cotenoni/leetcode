from typing import List

#https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            middle = start + (end - start) // 2

            if nums[middle] == target:
                return middle
                
            elif nums[start] <= nums[middle]:
                if nums[start] <= target <= nums[middle]:
                    end = middle - 1 
                else:
                    start = middle + 1
            else:
                if nums[middle] <= target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        return -1
        


sol = Solution()
print(sol.search([0,1,2,4,5,6,7], 4)) #3
print(sol.search([4,5,6,7,0,1,2], 0)) #4
print(sol.search([4,5,6,7,0,1,2], 5)) #1
print(sol.search([4,5,6,7,0,1,2], 3)) #-1
print(sol.search([1], 0)) #-1
print(sol.search([4,5,6,0,1,2,3], 5)) #1
print(sol.search([3,5,1], 3)) #0
print(sol.search([1,3],3)) #1

[4,5,6,0,1,2,3]
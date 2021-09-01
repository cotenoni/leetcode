from typing import List

#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: #nums[mid] < nums[right]:
                right = mid

            # [3,3,1,3]
            #  l m   r 
            # [0,1,4,4,5,6,7]
            # [5,6,7,4,4,4,4]
            # [5,6,0,4,4,4,4]
            # [6,0,4,4,4,4,4]
            

        return nums[left]



sol = Solution()
# print(sol.findMin([3,4,5,1,2]) == 1)
# print(sol.findMin([4,5,6,7,0,1,2]) == 0)
# print(sol.findMin([11,13,15,17]) == 11)
# print(sol.findMin([1]) == 1)

# print(sol.findMin([5,6,7,4,4,4,4]) == 4)
# print(sol.findMin([5,6,0,4,4,4,4]) == 0)
# print(sol.findMin([6,0,4,4,4,4,4]) == 0)
# print(sol.findMin([2,2,2,0,1]) == 0)

print(sol.findMin([3,3,1,3]) == 1)
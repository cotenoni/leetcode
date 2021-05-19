from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        numsCopy = nums.copy()
        newIndex = 0
        
        for i in range(length):
            newIndex = i

            for j in range(k):
                if newIndex < length - 1:
                    newIndex += 1
                else:
                    newIndex = 0

            nums[newIndex] = numsCopy[i]

        print(nums)
        

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)
solution.rotate([1,2], 3)



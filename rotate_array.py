from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        newList = nums.copy()
        cpt = 0
        
        for i in range(length):
            if i + k < length:
                nums[i + k] = newList[i]
            else:
                nums[cpt] = newList[i]
                cpt += 1

        print(nums)
        

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)



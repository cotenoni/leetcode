import bisect
from typing import List


#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1


sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) #[1,2]
print(sol.twoSum([2,3,4], 6)) #[1,3]
print(sol.twoSum([-1,0], -1)) #[1,2]
print(sol.twoSum([0,0,3,4], 0)) #[1,2]
print(sol.twoSum([5,25,75], 100)) #[2,3]
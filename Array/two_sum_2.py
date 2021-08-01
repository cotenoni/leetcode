import bisect
from typing import List


#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            remaining = target - numbers[i]

            bisect_index = bisect.bisect_left(numbers[i + 1:], remaining) + i + 1
            if bisect_index < len(numbers) and numbers[bisect_index] == remaining:
                return [i + 1, bisect_index + 1]


sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) #[1,2]
print(sol.twoSum([2,3,4], 6)) #[1,3]
print(sol.twoSum([-1,0], -1)) #[1,2]
print(sol.twoSum([0,0,3,4], 0)) #[1,2]
print(sol.twoSum([5,25,75], 100)) #[2,3]
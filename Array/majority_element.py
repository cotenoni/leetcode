import collections
from typing import List

#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


sol = Solution()
print(sol.majorityElement([3,2,3]) == 3)
print(sol.majorityElement([2,2,1,1,1,2,2]) == 2)
print(sol.majorityElement([2]) == 2)

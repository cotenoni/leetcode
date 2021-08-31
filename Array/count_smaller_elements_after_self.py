from typing import List
from sortedcontainers import SortedList


#https://leetcode.com/problems/count-of-smaller-numbers-after-self/
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = SortedList()
        answer = []

        for i in range(len(nums) - 1, -1, -1):
            pos = sorted_list.bisect_left(nums[i])
            answer.append(pos)
            sorted_list.add(nums[i])

        return reversed(answer)


sol = Solution()
print(sol.countSmaller([-1]) == [0])
print(sol.countSmaller([-1, -1]) == [0, 0])
print(sol.countSmaller([5,2,6,1]) == [2,1,1,0])

from typing import List


#https://leetcode.com/problems/count-of-smaller-numbers-after-self/
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)

        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
                    count += 1

            answer[i] = count

        return answer



sol = Solution()
print(sol.countSmaller([-1]) == [0])
print(sol.countSmaller([-1, -1]) == [0, 0])
print(sol.countSmaller([5,2,6,1]) == [2,1,1,0])

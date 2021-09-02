from typing import List

#https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        ans = 0

        for n in nums:
            cnt = 0
            
            while not visited[n]:
                cnt += 1
                visited[n] = True
                n = nums[n]

            ans = max(ans, cnt)

        return ans
            

sol = Solution()
print(sol.arrayNesting([5,4,0,3,1,6,2]) == 4)
print(sol.arrayNesting([0,1,2]) == 1)
print(sol.arrayNesting([0]) == 1)
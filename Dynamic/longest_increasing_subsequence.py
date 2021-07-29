from typing import List
import bisect


#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       #REDO again ?
       pass


solution = Solution()
# print(solution.lengthOfLIS([10])) #1
# print(solution.lengthOfLIS([10,9,2,5,1,3,7,1,101,18])) #4
# print(solution.lengthOfLIS([0,1,0,3,2,3])) #4
# print(solution.lengthOfLIS([7,7,7,7,7,7,7])) #1
# print(solution.lengthOfLIS([9,8,7,6,5,4,3,2,1])) #1
# print(solution.lengthOfLIS([9,8,7,6,5,4,3,2,10])) #2
# print(solution.lengthOfLIS([1,2,3,4,5])) #5
# print(solution.lengthOfLIS([1,0,1,0,1,0,1])) #2
print(solution.lengthOfLIS([1,0,2,1,3,0])) #3

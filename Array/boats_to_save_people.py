import math
from typing import List

#https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats_count = 0
        start, end = 0, len(people) -1

        people.sort()

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                end -= 1
                
            boats_count += 1
            
        return boats_count
        

sol = Solution()
print(sol.numRescueBoats([1], 1)) #1
print(sol.numRescueBoats([1,2], 3)) #1
print(sol.numRescueBoats([3,2,2,1], 3)) #3
print(sol.numRescueBoats([3,5,3,4], 5)) #4
print(sol.numRescueBoats([1, 3, 1, 2, 3, 1], 3)) #4
print(sol.numRescueBoats([21,40,16,24,30], 50)) #3

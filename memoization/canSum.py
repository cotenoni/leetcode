from typing import Dict, List
import functools

class Solution:
    def canSum(self, target:int, numbers: List[int], memo = None) -> bool:
        if memo == None:
            memo = {}

        if target in memo:
            return memo[target]

        if target == 0:
            return True
        
        if target < 0:
            return False
        
        for n in numbers:
            remainder = target - n
            if self.canSum(remainder, numbers, memo):
                memo[target] = True
                return True

        memo[target] = False
        return False

        
solution = Solution()
print(solution.canSum(7, [2, 3])) #expected: true
print(solution.canSum(7, [5, 3, 4, 7])) #expected: true
print(solution.canSum(7, [2, 4])) #expected: false
print(solution.canSum(8, [2, 3, 5])) #expected: true
print(solution.canSum(300, [7, 14])) #expected: false
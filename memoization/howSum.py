from typing import List


class Solution:
    def howSum(self, target:int, numbers: List[int], memo = None) -> List[int]:
        if memo == None:
            memo = {}

        if target in memo:
            return memo[target]

        if target == 0:
            return []
        
        if target < 0:
            return None
        
        for n in numbers:
            remainder = target - n
            remainderResult = self.howSum(remainder, numbers, memo)

            if remainderResult != None:
                remainderResult.append(n)
                memo[target] = remainderResult
                return remainderResult

        memo[target] = None
        return None

        
solution = Solution()
print(solution.howSum(7, [2, 3])) #expected: [3, 2, 2]
print(solution.howSum(7, [5, 3, 4, 7])) #expected: [4, 3]
print(solution.howSum(7, [2, 4])) #expected: None
print(solution.howSum(8, [2, 3, 5])) #expected: [2, 2, 2, 2]
print(solution.howSum(300, [7, 14])) #expected: None
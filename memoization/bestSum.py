from typing import List


class Solution:
    def bestSum(self, target:int, numbers: List[int], memo = None) -> List[int]:
        if memo is None:
            memo = {}
        
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None

        shortestCombination = None
        for n in numbers:
            remainder = target - n
            remainderCombination = self.bestSum(remainder, numbers, memo)

            if remainderCombination is not None:
                remainderCombination = remainderCombination.copy()
                remainderCombination.append(n)

                if shortestCombination is None or len(remainderCombination) < len(shortestCombination):
                    shortestCombination = remainderCombination.copy()

        memo[target] = shortestCombination
        return shortestCombination

        
solution = Solution()
print(solution.bestSum(7, [5, 3, 4, 7])) #expected: [7]
print(solution.bestSum(8, [1, 4, 5])) #expected: [4, 4]
print(solution.bestSum(8, [2, 3, 5])) #expected: [3, 5]
print(solution.bestSum(100, [1, 2, 5, 25])) #expected: [25, 25, 25, 25]
from typing import List


class Solution:
    def bestSum(self, target:int, numbers: List[int]) -> List[int]:
        if target == 0:
            return []
        
        if target < 0:
            return None

        result = []

        for n in numbers:
            remainder = target - n
            remainderResult = self.bestSum(remainder, numbers)

            if remainderResult != None and (len(remainderResult) <= len(result) or len(result) == 0):
                result = remainderResult
                result.append(n)

        if len(result) == 0:
            return None

        return result

        
solution = Solution()
print(solution.bestSum(7, [5, 3, 4, 7])) #expected: [7]
print(solution.bestSum(7, [2, 4])) #expected: None
print(solution.bestSum(8, [2, 3, 5])) #expected: [3, 5]
#print(solution.bestSum(300, [7, 14])) #expected: None
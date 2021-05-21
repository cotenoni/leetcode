from typing import List


class Solution:
    def howSum(self, target:int, numbers: List[int], values = None) -> List[int]:
        if values == None:
            values = []

        if target == 0:
            return []
        
        if target < 0:
            return None
        
        for n in numbers:
            remainder = target - n
            if self.howSum(remainder, numbers, values) != None:
                values.append(n)
                return values

        return None

        
solution = Solution()
print(solution.howSum(7, [2, 3])) #expected: true
print(solution.howSum(7, [5, 3, 4, 7])) #expected: true
print(solution.howSum(7, [2, 4])) #expected: false
print(solution.howSum(8, [2, 3, 5])) #expected: true
#print(solution.howSum(300, [7, 14])) #expected: false
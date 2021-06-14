from typing import List

#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):            
            if digits[i] == 9:
                digits[i] = 0

                if i == 0:
                    digits = [1] + digits
            else:
                digits[i] = digits[i] + 1
                break;

        return digits
            

solution = Solution()
print(solution.plusOne([1, 2, 3])) # [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
print(solution.plusOne([0])) # [1]
print(solution.plusOne([9, 9])) # [1, 0, 0]


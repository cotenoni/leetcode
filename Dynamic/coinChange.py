from typing import List

#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        if amount == 0:
            return 0

        table = [0] * (amount + 1)
        table[0] = 1

        for i in range(amount + 1):
            current = table[i]

            if current > 0:
                for c in coins:
                    if i + c <= amount and (table[i + c] == 0 or current < table[i + c]):
                        table[i + c] = table[i] + 1

        return table[amount] - 1

solution = Solution()
print(solution.coinChange([1, 2, 5], 11)) #3
print(solution.coinChange([2], 3)) #-1
print(solution.coinChange([1], 0)) #0
print(solution.coinChange([1], 1)) #1
print(solution.coinChange([1], 2)) #2
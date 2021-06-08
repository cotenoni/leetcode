from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentBestPrice = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                priceBeingEvaluated = prices[j] - prices[i]

                if priceBeingEvaluated > currentBestPrice :
                    currentBestPrice = priceBeingEvaluated

        return currentBestPrice


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(solution.maxProfit([7,6,4,3,1])) # 0
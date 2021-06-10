from typing import List

#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentBestPrice = 0
        currentMin = prices[0]

        for i in range(1, len(prices)):
            currentMin = min(currentMin, prices[i])
            currentBestPrice = max(currentBestPrice, prices[i] - currentMin)

        return currentBestPrice


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4])) # 5
print(solution.maxProfit([7,6,4,3,1])) # 0
print(solution.maxProfit([7,3,10,1,6])) # 7
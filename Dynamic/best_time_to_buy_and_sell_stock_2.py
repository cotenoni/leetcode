from typing import List

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min, current_profit, profit_so_far = prices[0], 0, 0
        
        for i in range(1, len(prices)):
            current_profit = max(current_profit, prices[i] - current_min)
            current_min = min(current_min, prices[i])

            if prices[i] < prices[i - 1]:
                profit_so_far += current_profit
                current_profit = 0
                current_min = prices[i]
                
        profit_so_far += current_profit
        #print(current_min, current_profit, profit_so_far)

        return profit_so_far
        

sol = Solution()
print(sol.maxProfit([7,1,3,5,3,6,4]) == 7)
print(sol.maxProfit([1,2,3,4,5]) == 4)
print(sol.maxProfit([7,6,4,3,1]) == 0)
        
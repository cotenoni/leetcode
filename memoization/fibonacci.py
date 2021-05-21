

class Solution:
    #https://leetcode.com/problems/fibonacci-number/
    def fib(self, n:int, memo = {}) -> int:
        if n in memo:
            return memo[n]

        if n <= 1:
            return 1

        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]


solution = Solution()
print(solution.fib(6)) #expected: 8
print(solution.fib(7)) #expected: 13
print(solution.fib(8)) #expected: 31
print(solution.fib(50)) #expected: 12586269025
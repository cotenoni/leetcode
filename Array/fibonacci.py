

class Solution:
    def fib(self, n:int) -> int:
        if n == 0:
            return 0
            
        if n <= 2:
            return 1
        
        return self.fib(n - 1) + self.fib(n - 2)


solution = Solution()
print(solution.fib(6)) #expected: 8
print(solution.fib(7)) #expected: 13
print(solution.fib(8)) #expected: 31
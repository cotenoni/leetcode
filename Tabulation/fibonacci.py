

class Solution:
    #https://leetcode.com/problems/fibonacci-number/
    def fib(self, n:int) -> int:
        table = [0] * (n + 1)
        table[1] = 1

        for i in range(len(table) - 1):
            table[i + 1] += table[i];

            if i + 2 < len(table):
                table[i + 2] += table[i];

        return table[n]


solution = Solution()
print(solution.fib(6)) #expected: 8
print(solution.fib(7)) #expected: 13
print(solution.fib(8)) #expected: 21
print(solution.fib(51)) #expected: 20365011074
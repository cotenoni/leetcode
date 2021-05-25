

class Solution:
    #https://leetcode.com/problems/fibonacci-number/
    def fib(self, n:int) -> int:
        array = [0] * (n + 1)

        for i in range(len(array)):
            if i <= 1:
                array[i] = i
            else:
                array[i] = array[i - 1] + array [i - 2]

        return array[n]


solution = Solution()
print(solution.fib(6)) #expected: 8
print(solution.fib(7)) #expected: 13
print(solution.fib(8)) #expected: 21
print(solution.fib(51)) #expected: 20365011074
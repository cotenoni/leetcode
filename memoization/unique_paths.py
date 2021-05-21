class Solution:
    # https://leetcode.com/problems/unique-paths/
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if (m, n) in memo:
            return memo[(m, n)]

        if m == 1 and n == 1:
            return 1

        bottom = 0
        right = 0

        if m > 1:
            bottom = self.uniquePaths(m - 1, n)

        if n > 1:
            right = self.uniquePaths(m, n - 1)

        memo[(m, n)] = bottom + right
        return memo[(m, n)]


solution = Solution()
print(solution.uniquePaths(3, 7)) #expected: 28
print(solution.uniquePaths(3, 2)) #expected: 3
print(solution.uniquePaths(3, 3)) #expected: 6

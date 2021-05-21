class Solution:
    # https://leetcode.com/problems/unique-paths/
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if (m, n) in memo:
            return memo[(m, n)]

        if m == 1 and n == 1:
            return 1

        if m == 0 or n == 0:
            return 0

        memo[(m, n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
        return memo[(m, n)]


solution = Solution()
print(solution.uniquePaths(3, 7)) #expected: 28
print(solution.uniquePaths(3, 2)) #expected: 3
print(solution.uniquePaths(3, 3)) #expected: 6

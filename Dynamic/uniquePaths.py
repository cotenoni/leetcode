#https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/
class Solution:
    def uniquePaths(self, m: int, n: int, memo=None) -> int:
        # m = number of lines
        # n = number of columns
        if memo is None:
            memo = {}

        if (m, n) in memo:
            return memo[(m, n)]

        if m == 1 and n == 1: 
            return 1

        if m == 0 or n == 0:
            return 0
        
        memo[(m, n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
        return memo[(m, n)]

      
    
    # def uniquePaths(self, m: int, n: int) -> int:
    #     # m = number of lines
    #     # n = number of columns
    #     grid = [ [0]*n for i in range(m)]
    #     grid[0][0] = 1
        
    #     for i in range(m):
    #         for j in range(n):
    #             currentCoordinateWays = grid[i][j]
    #             if i + 1 < m:
    #                 grid[i + 1][j] += currentCoordinateWays
                
    #             if j + 1 < n:
    #                 grid[i][j+1] += currentCoordinateWays

    #     return grid[m - 1][n - 1]
            

solution = Solution()
print(solution.uniquePaths(3, 7)) #28
print(solution.uniquePaths(3, 2)) #3
print(solution.uniquePaths(3, 3)) #6
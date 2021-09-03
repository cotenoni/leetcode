from typing import List
from functools import lru_cache

#https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}

        def dfs(x, y):
            if (x, y) in visited: 
                return visited[(x,y)]

            longest_sub_path = 0
            for (new_x, new_y) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if new_x >= 0 and new_x < len(matrix) and new_y >= 0 and new_y < len(matrix[new_x]) and matrix[x][y] < matrix[new_x][new_y]:
                    longest_sub_path = max(longest_sub_path, dfs(new_x, new_y) + 1)

            visited[(x, y)] = longest_sub_path
            return longest_sub_path

        longest_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                longest_path = max(longest_path, dfs(i, j) + 1)

        return longest_path


sol = Solution()
print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4)
print(sol.longestIncreasingPath( [[3,4,5],[3,2,6],[2,2,1]]) == 4)
print(sol.longestIncreasingPath([[1]]) == 1)
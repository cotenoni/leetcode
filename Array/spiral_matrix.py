from typing import List

#https://leetcode.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        possibles_direction = [(0,1), (1,0), (0,-1), (-1,0)]
        current_direction = possibles_direction[0]
        x = y = 0
        m, n = len(matrix), len(matrix[0])

        while matrix[x][y] > -101:
            ans.append(matrix[x][y])
            matrix[x][y] = -101

            new_x, new_y = x + current_direction[0], y + current_direction[1]
            if new_x in range(0, m) and new_y in range(0, n) and matrix[new_x][new_y] > -101:
                x, y = new_x, new_y
                continue

            for new_direction in possibles_direction:
                new_x, new_y = x + new_direction[0], y + new_direction[1]
                if new_x in range(0, m) and new_y in range(0, n) and matrix[new_x][new_y] > -101:
                    x, y = new_x, new_y
                    current_direction = new_direction
                    break
        print(ans)
        return ans


sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5])

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7])

matrix = [[1,2,3,4]]
print(sol.spiralOrder(matrix) == [1,2,3,4])

matrix = [[1], [2], [3], [4]]
print(sol.spiralOrder(matrix) == [1,2,3,4])
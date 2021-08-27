import copy
from typing import List

#https://leetcode.com/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies, as if by over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        """
        initial_board = copy.deepcopy(board)
        
        for row_idx, row in enumerate(initial_board):
            for col_idx, value in enumerate(row):
                nb_live_neighbors = self.get_neighbors_count(initial_board, row_idx, col_idx)

                if value == 1 and (nb_live_neighbors < 2 or nb_live_neighbors > 3):
                    board[row_idx][col_idx] = 0
                elif value == 0 and nb_live_neighbors == 3:
                    board[row_idx][col_idx] = 1
                
                    
    def get_neighbors_count(self, initial_board, row_idx, col_idx):
        nb_live_neighbors = 0
        if row_idx > 0:
            if col_idx > 0:
                nb_live_neighbors += initial_board[row_idx - 1][col_idx - 1] 
            nb_live_neighbors += initial_board[row_idx - 1][col_idx]
            if col_idx < len(initial_board[row_idx]) - 1:
                nb_live_neighbors += initial_board[row_idx - 1][col_idx + 1]
        
        if row_idx < len(initial_board) - 1:
            if col_idx > 0:
                nb_live_neighbors += initial_board[row_idx + 1][col_idx - 1] 
            nb_live_neighbors += initial_board[row_idx + 1][col_idx]
            if col_idx < len(initial_board[row_idx]) - 1:
                nb_live_neighbors += initial_board[row_idx + 1][col_idx + 1]
        
        if col_idx > 0:
            nb_live_neighbors += initial_board[row_idx][col_idx - 1] 
        if col_idx < len(initial_board[row_idx]) - 1:
                nb_live_neighbors += initial_board[row_idx][col_idx + 1]

        return nb_live_neighbors


sol = Solution()
print(sol.gameOfLife([[1]]) == [[0]])
print(sol.gameOfLife([[0]]) == [[0]])
print(sol.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]) == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
print(sol.gameOfLife([[1,1],[1,0]]) == [[1,1],[1,1]])

        
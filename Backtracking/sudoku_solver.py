from typing import List
from itertools import product

#https://leetcode.com/problems/sudoku-solver/
class Solution:

    BOARD_SIZE = 9
    SUBBOX_SIZE = 3
    DIGITS = set([str(num) for num in range(1, BOARD_SIZE + 1)])
    EMPTY = '.'
    

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.search(board)


    def search(self, board):
        if self.is_valid_state(board):
            return True

        for row_num, row in enumerate(board):
            for col_num, element in enumerate(row):
                if element == self.EMPTY:
                    for candidate in self.get_candidates(board, row_num, col_num):
                        board[row_num][col_num] = candidate
                        if self.search(board):
                            return True
                        else:
                            board[row_num][col_num] = self.EMPTY
                        
                    return False        
        return True

    def is_valid_state(self, board):
        for row in self.get_rows(board):
            if set(row) != self.DIGITS:
                return False

        for col in self.get_cols(board):
            if set(col) != self.DIGITS:
                return False

        for grid in self.get_grids(board):
            if set(grid) != self.DIGITS:
                return False
            
        return True

    def get_candidates(self, board, x, y):
        used_digits = set()
        used_digits.update(self.get_kth_row(board, x))
        used_digits.update(self.get_kth_col(board, y))
        used_digits.update(self.get_grid_at_row_col(board, x, y))
        used_digits -= set([self.EMPTY])
        
        return self.DIGITS - used_digits

    def get_rows(self, board):
        for i in range(self.BOARD_SIZE):
            yield board[i]

    def get_kth_row(self, board, k):
        return board[k]

    def get_cols(self, board):
        for col in range(self.BOARD_SIZE):
            ret = [
                board[row][col] for row in range(self.BOARD_SIZE)
            ]
            yield ret

    def get_kth_col(self, board, k):
        return [row[k] for row in self.get_rows(board)]

    def get_grids(self, board):
        for row in range(0, self.BOARD_SIZE, self.SUBBOX_SIZE):
            for col in range(0, self.BOARD_SIZE, self.SUBBOX_SIZE):
                grid = [
                    board[r][c] for r, c in 
                    product(range(row, row + self.SUBBOX_SIZE), range(col, col + self.SUBBOX_SIZE))
                ]
                yield grid

    def get_grid_at_row_col(self, board, row, col):
        row = row // self.SUBBOX_SIZE * self.SUBBOX_SIZE
        col = col // self.SUBBOX_SIZE * self.SUBBOX_SIZE

        return [
            board[r][c] for r, c in 
            product(range(row, row + self.SUBBOX_SIZE), range(col, col + self.SUBBOX_SIZE))
        ]   
        

sol = Solution()
board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
sol.solveSudoku(board)
print(board)
print(board == [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
    ])
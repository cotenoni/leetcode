from typing import List

#https://leetcode.com/problems/n-queens/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def search(self, state, solutions, n):
        if len(state) == n:
            solutions.append(self.state_to_string(state, n))
            return
        
        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        position = len(state)
        candidates = set(range(n))

        for row, col in enumerate(state):
            candidates.discard(col)
            distance = position - row
            candidates.discard(col + distance)
            candidates.discard(col - distance)
        return candidates

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            ret.append('.' * i + 'Q' + '.' * (n - i - 1))
        return ret
        

sol = Solution()
print(sol.solveNQueens(1))
print(sol.solveNQueens(4))
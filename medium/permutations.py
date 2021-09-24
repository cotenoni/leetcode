from typing import List

#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.solutions = []
        self.state = []
        self.search()
        return self.solutions

    def search(self):
        if self.is_valid_state():
            self.solutions.append(self.state.copy())
            return

        for candidate in self.get_candidates():
            self.state.append(candidate)
            self.search()
            self.state.pop()

    def get_candidates(self):
        if not self.state:
            return [value for value in self.nums]

        candidates = set(self.nums)
        for num in self.nums:
            if num in self.state:
                candidates.discard(num)
        return candidates

    def is_valid_state(self):
        return len(self.nums) == len(self.state)


sol = Solution()
print(sol.permute([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute([0,1])) #[[0,1],[1,0]]
print(sol.permute([1])) #[[1]]
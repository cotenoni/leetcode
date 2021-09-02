from typing import List

#https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(graph, node, length, visited={}):
            if node in visited:
                return length

            visited[node] = True
            return dfs(graph, graph[node], length + 1, visited)
        
        graph = {i: num for i, num in enumerate(nums)}
        longest_path = 0
        
        for i in range(len(nums)):
            longest_path = max(dfs(graph, i, 0), longest_path)

        return longest_path
        

sol = Solution()
print(sol.arrayNesting([5,4,0,3,1,6,2]) == 4)
print(sol.arrayNesting([0,1,2]) == 1)
print(sol.arrayNesting([0]) == 1)
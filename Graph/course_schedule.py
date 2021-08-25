import collections
from typing import List

#https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        def has_cycle(course):
            if visited[course]:
                return True

            if not graph[course]:
                return False

            visited[course] = True
            for prerequisite in graph[course]:
                if has_cycle(prerequisite):
                    return True
            
            visited[course] = False
            return False
        
        visited = [False]*numCourses
        for course in graph:
            if has_cycle(course):
                return False

            graph[course] = []
        
        return True

sol = Solution()
print(sol.canFinish(1, []) == True)
print(sol.canFinish(1, [[0, 0]]) == False)
print(sol.canFinish(2, [[1,0]]) == True)
print(sol.canFinish(2, [[1,0], [0,1]]) == False)
print(sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]) == True)

# n = 4 (0, 1, 2, 3)
# [0, 1], [1, 2], [2, 0] 

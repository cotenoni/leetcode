from typing import List

#https://leetcode.com/problems/jump-game-iii/
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        min_pos = max_pos = start
        visited = {}
        queue = [start]

        while queue:
            current_pos = queue.pop()
            visited[current_pos] = True

            if arr[current_pos] == 0:
                return True

            min_pos = current_pos - arr[current_pos]
            max_pos = current_pos + arr[current_pos]

            if min_pos >= 0 and not min_pos in visited:
                queue.append(min_pos)

            if max_pos < len(arr) and not max_pos in visited:
                queue.append(max_pos)

        return False

sol = Solution()
print(sol.canReach([0], 0)) #True
print(sol.canReach([1], 0)) #False
print(sol.canReach([4,2,3,0,3,1,2], 5)) #True
print(sol.canReach([4,2,3,0,3,1,2], 0)) #True
print(sol.canReach([3,0,2,1,2], 2)) #False

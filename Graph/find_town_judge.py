import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trust_counts = collections.Counter([relation[1] for relation in trust])
        trusters_count = collections.Counter([relation[0] for relation in trust])
        candidate = trust_counts.most_common(1)
        
        if candidate and candidate[0][1] == n - 1:
            return candidate[0][0] if candidate[0][0] not in trusters_count else -1
        
        return -1

       


solution = Solution()
print(solution.findJudge(2, [[1,2]])) #2
print(solution.findJudge(3, [[1,3],[2,3]])) #3
print(solution.findJudge(3, [[1,3],[2,3],[3,1]])) #-1
print(solution.findJudge(3, [[1,2],[2,3]])) #-1
print(solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])) #3
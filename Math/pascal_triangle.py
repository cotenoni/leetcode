from typing import List

#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]

        for i in range(1, numRows):
            current = []
            prev = answer[i - 1]

            for j in range(len(prev)):
                if j == 0:
                    current.append(prev[j])
                else:
                    current.append(prev[j - 1] + prev[j])
                
            current.append(prev[len(prev) - 1])
            answer.append(current)
        return answer


sol = Solution()
print(sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
print(sol.generate(1) == [[1]])
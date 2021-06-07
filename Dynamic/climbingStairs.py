#https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1
        
        for i in range(n):
            current = table[i]

            for o in [1, 2]:
                if current and i + o <= n:
                    table[i + o] += current

        return table[n]

solution = Solution()
print(solution.climbStairs(2)) # 2
print(solution.climbStairs(3)) # 3
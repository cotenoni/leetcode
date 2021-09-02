
#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}

        while n not in visited:
            visited[n] = True
            sum_of_squares = 0

            while n != 0:
                d = n % 10
                sum_of_squares += d ** 2
                n //= 10

            if sum_of_squares == 1:
                return True

            n = sum_of_squares

        return False 


sol = Solution()
print(sol.isHappy(19) == True)
print(sol.isHappy(2) == False)
print(sol.isHappy(1) == True)

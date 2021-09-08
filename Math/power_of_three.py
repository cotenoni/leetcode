
#https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


sol = Solution()
print(sol.isPowerOfThree(0) == False)
print(sol.isPowerOfThree(27) == True)
print(sol.isPowerOfThree(9) == True)
print(sol.isPowerOfThree(45) == False)
print(sol.isPowerOfThree(2))
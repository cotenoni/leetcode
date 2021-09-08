
#https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n):
            if 3**i == n:
                return True

            if 3**i > n:
                return False

        return False


sol = Solution()
print(sol.isPowerOfThree(0) == False)
print(sol.isPowerOfThree(27) == True)
print(sol.isPowerOfThree(9) == True)
print(sol.isPowerOfThree(45) == False)
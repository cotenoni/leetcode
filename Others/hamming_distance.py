#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        nb, num_bits = 0, 31

        for i in range(num_bits):
            if (x >> i) & 1 != (y >> i) & 1:
                nb += 1

        return nb



solution = Solution()
print(solution.hammingDistance(1, 4)) #2
print(solution.hammingDistance(3, 1)) #1
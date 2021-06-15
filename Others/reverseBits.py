#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31

        while power >= 0:
            ret += (n & 1) << power
            n >>= 1
            power -= 1

        return ret


solution = Solution()

print(solution.reverseBits(43261596)) #964176192
print(solution.reverseBits(4294967293)) #3221225471 
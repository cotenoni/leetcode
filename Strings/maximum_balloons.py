import collections

#https://leetcode.com/problems/maximum-number-of-balloons/
class Solution:
    WORD = "balloon"

    def maxNumberOfBalloons(self, text: str) -> int:
        ans, characters_counts = 0, collections.Counter(text)

        while len(collections.Counter(self.WORD) - characters_counts) == 0:
            characters_counts = characters_counts - collections.Counter(self.WORD)
            ans += 1

        return ans
        

sol = Solution()
print(sol.maxNumberOfBalloons("leetcode") == 0)
print(sol.maxNumberOfBalloons("nlaebolko") == 1)
print(sol.maxNumberOfBalloons("loonbalxballpoon") == 2)
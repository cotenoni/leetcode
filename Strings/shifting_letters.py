from typing import List
import string

#https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        running_sum, ans = 0, ""

        for i in range(len(shifts) - 1, -1, -1):
            running_sum += shifts[i]
            running_sum = running_sum % 26
            index = ((ord(s[i]) - 97) + running_sum) % 26
            ans += string.ascii_lowercase[index]

        return ans[::-1]


sol = Solution()
print(sol.shiftingLetters("abc", [3,5,9]) == "rpl")
print(sol.shiftingLetters("aaa", [1,2,3]) == "gfd")
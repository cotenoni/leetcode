from typing import List
import string

#https://leetcode.com/problems/shifting-letters/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        running_sum, sums = 0, [0] * len(shifts)

        for i in range(len(shifts) - 1, -1, -1):
            running_sum += shifts[i]
            running_sum = running_sum % 26
            sums[i] = running_sum

        string_to_update = list(s)
        for i, c in enumerate(s):
            index = ((ord(c) - 97) + sums[i]) % 26
            string_to_update[i] = string.ascii_lowercase[index]

        return ''.join(string_to_update)


sol = Solution()
print(sol.shiftingLetters("abc", [3,5,9]) == "rpl")
print(sol.shiftingLetters("aaa", [1,2,3]) == "gfd")
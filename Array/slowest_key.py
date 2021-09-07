from typing import List
import collections

#https://leetcode.com/problems/slowest-key/
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration, ans = 0, ""

        for i, key in enumerate(keysPressed):
            duration = releaseTimes[i]
            if i > 0:
                duration -= releaseTimes[i - 1]
            
            if (duration == max_duration and key > ans) or duration > max_duration:
                max_duration = duration
                ans = key
        return ans

sol = Solution()
print(sol.slowestKey([9,29,49,50], "cbcd") == "c")
print(sol.slowestKey([12,23,36,46,62], "spuda") == "a")

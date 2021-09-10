import collections

#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = collections.Counter(s)
        t_counts = collections.Counter(t)

        return len(s_counts - t_counts) == 0 and len(t_counts - s_counts) == 0


sol = Solution()
# print(sol.isAnagram("anagram","nagaram") == True)
# print(sol.isAnagram("rat", "car") == False)
print(sol.isAnagram("a", "ab") == False)
import collections

#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts, t_counts = collections.defaultdict(int), collections.defaultdict(int)

        for i in range(len(s)):
            s_counts[s[i]] += 1

        for i in range(len(t)):
            t_counts[t[i]] += 1

        if len(t_counts) > len(s_counts):
            s_counts, t_counts = t_counts, s_counts

        for key, value in s_counts.items():
            if key not in t_counts or t_counts[key] != value:
                return False

        return True
        

sol = Solution()
print(sol.isAnagram("anagram","nagaram") == True)
print(sol.isAnagram("rat", "car") == False)
print(sol.isAnagram("a", "ab") == False)
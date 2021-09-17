from typing import List
import collections

#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            groups[sorted_s].append(s)

        return [*groups.values()]

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))


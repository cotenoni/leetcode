from typing import List


class Solution:
    def countConstruct(self, target:str, wordBank: List[str], memo = None) -> int:
        if memo == None:
            memo = {}

        if target in memo: return memo[target]
        if target == "": return 1

        constructCount = 0
        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                constructCount += self.countConstruct(suffix, wordBank, memo)

        memo[target] = constructCount            
        return constructCount
                
        
solution = Solution()
print(solution.countConstruct("", ["cat", "dog", "mouse"])) #expected: 1
print(solution.countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #expected: 1
print(solution.countConstruct("skateboard", ["sk", "ateboard", "skate", "board", "ska", "teboard", "boar"])) #expected: 3
print(solution.countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])) #expected: 0

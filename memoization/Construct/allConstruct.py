from typing import List


class Solution:
    def allConstruct(self, target:str, wordBank: List[str], memo = None) -> List[List[str]]:
        if memo is None:
            memo = {}
        
        if target in memo: return memo[target]
        if target == "": return [[]]

        result = []

        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                suffixWays = self.allConstruct(suffix, wordBank, memo)

                for way in suffixWays:
                    way.insert(0, word)

                result.extend(suffixWays)

        memo[target] = result.copy()    
        return result
                
        
solution = Solution()
print(solution.allConstruct("", ["cat", "dog", "mouse"])) #expected: [[]]
print(solution.allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])) #expected: [[ab, cd, ef], [ab, c, def], [abc, def], [abcd, ef]]
print(solution.allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) #expected: [[purp, le]]
print(solution.allConstruct("skateboard", ["sk", "ateboard", "skate", "board", "ska", "teboard", "boar"])) #expected: 
print(solution.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])) #expected: []

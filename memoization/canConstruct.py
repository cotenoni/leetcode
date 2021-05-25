from typing import List


class Solution:
    def canConstruct(self, target:str, wordBank: List[str], memo = None) -> bool:
        if memo == None:
            memo = {}

        if target in memo: return memo[target]
        if target == "": return True

        for word in wordBank:
            if target.startswith(word):
                remainingTarget = target[len(word):]

                if self.canConstruct(remainingTarget, wordBank, memo):
                    memo[target] = True
                    return True

        memo[target] = False
        return False
                
        
solution = Solution()
print(solution.canConstruct("", ["cat", "dog", "mouse"])) #expected: true
print(solution.canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) #expected: true
print(solution.canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) #expected: false
print(solution.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"])) #expected: false

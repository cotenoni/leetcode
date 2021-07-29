class Solution:
    def isValid(self, s: str) -> bool:
        correspondance = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for c in s:
            if c in correspondance:
                stack.append(c)
            else:
                if not stack or correspondance[stack.pop()] != c:
                    return False
        
        return len(stack) == 0
                    

sol = Solution()
print(sol.isValid("()") == True)
print(sol.isValid("()[]{}") == True)
print(sol.isValid("(]") == False)
print(sol.isValid("({[]})") == True)
print(sol.isValid("({[}])") == False)
print(sol.isValid("(") == False)
print(sol.isValid(")") == False)
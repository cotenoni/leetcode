
#https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1

        while start < end:
            while not s[start].isalpha() and start < end:
                start += 1

            while not s[end].isalpha() and start < end:
                end -= 1

            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
      
        return ''.join(s)


sol = Solution()
print(sol.reverseOnlyLetters("ab-cd") == "dc-ba")
print(sol.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba")
print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!")
print(sol.reverseOnlyLetters("-!%?") == "-!%?")
print(sol.reverseOnlyLetters("a") == "a")
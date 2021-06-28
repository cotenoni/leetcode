
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s: str, memo = None):
            if memo is None:
                memo = {}
            
            if s in memo:
                return memo[s]

            if len(s) == 0 or len(s) == 1:
                return True

            ret = False
            if s[0].lower() == s[len(s) - 1].lower():
                ret = is_palindrome(s[1:len(s)-1], memo)

            memo[s] = ret
            return ret

        memo = {}
        longest_palindrome = ""
        for i in range(len(s) + 1):
            for j in range(len(s), i, -1):
                str_to_evaluate = s[i:j]
               
                if is_palindrome(str_to_evaluate, memo) and len(str_to_evaluate) > len(longest_palindrome):
                    longest_palindrome = str_to_evaluate

        return longest_palindrome
            


solution = Solution()
print(solution.longestPalindrome("babad")) #bab or aba
print(solution.longestPalindrome("cbbd")) #bb
print(solution.longestPalindrome("a")) #a
print(solution.longestPalindrome("ac")) #a
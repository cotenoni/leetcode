
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromMiddle(s: str, left: int, right: int) -> int:
            if s is None or left > right:
                return 0

            while left >= 0 and right < len(s) and s[left].lower() == s[right].lower():
                left -= 1
                right += 1
            
            return right - left - 1

        
        start, end = 0, 0

        for i in range(len(s)):
            length1 = expandFromMiddle(s, i, i)
            length2 = expandFromMiddle(s, i, i + 1)
            max_length = max(length1, length2)

            if max_length > end - start:
                start = i - ((max_length - 1) // 2)
                end = i + (max_length // 2)

        return s[start:end + 1]



            


solution = Solution()
print(solution.longestPalindrome("racecar")) #bab or aba
print(solution.longestPalindrome("babad")) #bab or aba
print(solution.longestPalindrome("cbbd")) #bb
print(solution.longestPalindrome("a")) #a
print(solution.longestPalindrome("ac")) #a
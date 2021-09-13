import string

#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            left_character = s[start].lower()
            right_character = s[end].lower()

            if left_character not in string.ascii_lowercase and left_character not in string.digits:
                start += 1
                continue
            
            if right_character not in string.ascii_lowercase and right_character not in string.digits:
                end -= 1
                continue

            if right_character != left_character:
                return False

            start += 1
            end -= 1

        return True
        

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama") == True)
print(sol.isPalindrome("race a car") == False)
print(sol.isPalindrome("0P") == False)



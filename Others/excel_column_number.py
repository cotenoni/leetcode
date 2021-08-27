import string

#https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, c in enumerate(columnTitle):
            c_value = string.ascii_uppercase.index(c) + 1

            if  i < len(columnTitle) - 1:
                result += 26 ** (len(columnTitle) - i - 1) * c_value
            else:
                result += c_value
        
        return result

sol = Solution()
print(sol.titleToNumber("A") == 1)
print(sol.titleToNumber("Z") == 26)
print(sol.titleToNumber("AB") == 28)
print(sol.titleToNumber("BB") == 54)
print(sol.titleToNumber("ZY") == 701)
print(sol.titleToNumber("AAA") == 703)
print(sol.titleToNumber("FXSHRXW") == 2147483647)

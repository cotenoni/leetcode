import string

#https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        """
        s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
        """
        stack = []
        currentNumber = 0
        operation = "+"

        for i, c in enumerate(s):            
            if c.isdigit():
                currentNumber = currentNumber * 10 + int(c)
            
            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
                if operation == "-":
                    stack.append(-currentNumber)
                elif operation == "+":
                    stack.append(currentNumber)
                elif operation == "*":
                    stack.append(stack.pop() * currentNumber)
                else:
                    stack.append(int(stack.pop() / currentNumber))
                
                currentNumber = 0
                operation = c

        return sum(stack)
        


sol = Solution()
print(sol.calculate("3") == 3)
print(sol.calculate(" 15 ") == 15)
print(sol.calculate("3+2*2") == 7)
print(sol.calculate(" 3/2 ") == 1)
print(sol.calculate(" 3+5 / 2 ") == 5)
print(sol.calculate("3 + 5 - 2 + 6 * 3") == 24)
print(sol.calculate("5-2") == 3)
print(sol.calculate("1*2-3/4+5*6-7*8+9/10") == -24)
print(sol.calculate("10-3/2") == 9)

#1*2-3/4+5*6-7*8+9/10
#2-0+30-56+0
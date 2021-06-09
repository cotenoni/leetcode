from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n + 1):
            text = str(i)
            if i % 3 == 0 and i % 5 == 0:
                text = "FizzBuzz"
            elif i % 3 == 0:
                text = "Fizz"
            elif i % 5 == 0:
                text = "Buzz"

            answer.append(text)
        
        return answer
        



solution = Solution()
print(solution.fizzBuzz(3)) # ["1","2","Fizz"]
print(solution.fizzBuzz(5)) # ["1","2","Fizz","4","Buzz"]
print(solution.fizzBuzz(15)) # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
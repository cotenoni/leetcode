import collections

#https://leetcode.com/problems/count-largest-group/
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = collections.Counter()

        for i in range(1, n + 1):
            current_number, sum = i, 0

            while current_number:
                digit = current_number % 10
                sum += digit
                current_number //= 10
       
            sums[sum] += 1
        
        largest_size, nb_of_largest_size = max(sums.values()), 0
        
        for val in sums.values():
            if val == largest_size:
                nb_of_largest_size += 1

        return nb_of_largest_size
        

sol = Solution()
print(sol.countLargestGroup(1) == 1)
print(sol.countLargestGroup(13) == 4)
print(sol.countLargestGroup(2) == 2)
print(sol.countLargestGroup(15) == 6)
print(sol.countLargestGroup(24) == 5)
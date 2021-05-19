from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = dict()

        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]] = i

        return False


solution = Solution()
print(solution.containsDuplicate([1,2,3,1])) #expected: true
print(solution.containsDuplicate([1,2,3,4])) #expected: false
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # expected: true
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    output.append(nums1[i])
                    break

        return output


solution = Solution()
print(solution.intersect([1,2,2,1], [2,2])) #expected: [2,2]
print(solution.intersect([4,9,5], [9,4,9,8,4])) #expected: [4,9]
print(solution.intersect([1,2,2,1], [2])) #expected: [2]
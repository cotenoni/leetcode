# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= 4: return True

    return False

class Solution:
    def firstBadVersion(self, n):
        found = False

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

solution = Solution()
print(solution.firstBadVersion(4)) # 4
print(solution.firstBadVersion(5)) # 4
print(solution.firstBadVersion(10)) # 4
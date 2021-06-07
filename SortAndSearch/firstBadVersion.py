# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= 4: return True

    return False

class Solution:
    def firstBadVersion(self, n):
        found = False

        minimum = 0
        maximum = n

        while not found:
            index = minimum + max(((maximum - minimum) // 2), 1)
            isCurrentVersionBad = isBadVersion(index)
            isPreviousVersionBad = isBadVersion(index - 1)

            if isCurrentVersionBad and not isPreviousVersionBad:
                found = True
                continue
            
            if isCurrentVersionBad:
                maximum = index
            else:
                minimum = index

        return index

solution = Solution()
print(solution.firstBadVersion(4)) # 4
print(solution.firstBadVersion(5)) # 4
print(solution.firstBadVersion(10)) # 4
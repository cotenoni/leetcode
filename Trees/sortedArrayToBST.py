from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums) == 0: 
            return None

        if len(nums) == 1: 
            return TreeNode(nums[0])

        middle = int(len(nums) / 2)

        node = TreeNode(
            nums[middle],
            self.sortedArrayToBST(nums[:middle]),
            self.sortedArrayToBST(nums[middle+1:])
        )
    
        return node

solution = Solution()
print(solution.sortedArrayToBST(None))

solution = Solution()
nums = [1]
print(solution.sortedArrayToBST(nums))

solution = Solution()
nums = [1, 3]
print(solution.sortedArrayToBST(nums))

solution = Solution()
nums = [-10, -3, 0, 5, 9]
print(solution.sortedArrayToBST(nums)) # TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))

solution = Solution()
nums = [-10, -3, 0, 3, 5, 9]
print(solution.sortedArrayToBST(nums)) # TreeNode(3, TreeNode(-3, TreeNode(-10), TreeNode(0)), TreeNode(9, TreeNode(5)))







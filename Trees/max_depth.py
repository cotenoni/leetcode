from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth_helper(root, depth=0):
            if not root:
                return depth

            return max(max_depth_helper(root.left, depth + 1), max_depth_helper(root.right, depth + 1))

        return max_depth_helper(root)



sol = Solution()
print(sol.maxDepth(None) == 0)
print(sol.maxDepth(TreeNode(1)) == 1)

root = TreeNode(1, None, TreeNode(2))
print(sol.maxDepth(root) == 2)

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.maxDepth(root) == 3)


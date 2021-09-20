from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        value = str(self.val)
        value += ", " + (str(self.left) if self.left else "null")
        value += ", " + (str(self.right) if self.right else "null")

        return value

#https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


sol = Solution()
N = TreeNode

root = N(4, N(2, N(1), N(3)), N(7, N(6), N(9)))
print(sol.invertTree(root))

root = N(2, N(1), N(3))
print(sol.invertTree(root))

print(sol.invertTree(None))

root = N(4, N(2, N(1), N(3)), N(7, N(6)))
print(sol.invertTree(root))
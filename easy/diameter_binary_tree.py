from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1

        
sol = Solution()
N = TreeNode

root = N(1, N(2, N(4), N(5)), N(3))
print(sol.diameterOfBinaryTree(root)) #3 path of [4,2,1,3]

root = N(1, N(2))
print(sol.diameterOfBinaryTree(root)) #1

root = N(1, N(2, N(4, N(10, N(11, N(12, N(13))))), N(5, N(20, N(21, N(22, N(23)))))), N(3))
print(sol.diameterOfBinaryTree(root)) #10
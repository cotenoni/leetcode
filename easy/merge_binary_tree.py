# Definition for a binary tree node.
from typing import Optional


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

#https://leetcode.com/problems/merge-two-binary-trees/   
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1
        
        return TreeNode(
            root1.val + root2.val,
            self.mergeTrees(root1.left, root2.left),
            self.mergeTrees(root1.right, root2.right)
        )


sol = Solution()
N = TreeNode

print(sol.mergeTrees(None, None))
print(sol.mergeTrees(None, N(1, N(2))))
print(sol.mergeTrees(N(1, N(2)), None))

root1 = N(1, N(3, N(5)), N(2))
root2 = N(2, N(1, None, N(4)), N(3, None, N(7)))
print(sol.mergeTrees(root1, root2))

root1 = N(1)
root2 = N(1, N(2))
print(sol.mergeTrees(root1, root2))

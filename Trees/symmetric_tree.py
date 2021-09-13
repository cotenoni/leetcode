# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def are_subtrees_symmetric(left_subtree, right_subtree):
            if not left_subtree and not right_subtree:
                return True

            if not left_subtree or not right_subtree or left_subtree.val != right_subtree.val:
                return False

            return (are_subtrees_symmetric(left_subtree.left, right_subtree.right) 
                and are_subtrees_symmetric(left_subtree.right, right_subtree.left))

        return are_subtrees_symmetric(root.left, root.right)


T = TreeNode
sol = Solution()

#print(sol.isSymmetric(None) == False)

root = T(1)
print(sol.isSymmetric(root) == True)

root = T(1, T(2), T(2))
print(sol.isSymmetric(root) == True)

root = T(1, T(2, T(3), T(4)), T(2, T(4), T(3)))
print(sol.isSymmetric(root) == True)

root = T(1, T(2, None, T(3)), T(2, None, T(3)))
print(sol.isSymmetric(root) == False)

root = T(5, T(2, T(4, None, T(6)), T(3)), T(2, T(3), T(4, T(6))))
print(sol.isSymmetric(root) == True)

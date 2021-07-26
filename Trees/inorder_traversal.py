# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder_traversal_helper(node):
            if not node:
                return

            inorder_traversal_helper(node.left)
            traversal.append(node.val)
            inorder_traversal_helper(node.right)

        traversal = []
        inorder_traversal_helper(root)
        return traversal


solution = Solution()
tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(solution.inorderTraversal(tree)) #[1,3,2]



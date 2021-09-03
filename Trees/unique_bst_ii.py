from typing import List, Optional
import itertools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#https://leetcode.com/problems/unique-binary-search-trees-ii/
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(nodes_val):
            if not nodes_val:
                return [None]

            trees = []

            for i, val in enumerate(nodes_val):
                left_subtrees = helper(nodes_val[:i])
                right_subtrees = helper(nodes_val[i+1:])
                
                for (left, right) in itertools.product(left_subtrees, right_subtrees):
                    root = TreeNode(val, left, right)
                    trees.append(root)
            return trees

        nodes_val = [val for val in range(1, n + 1)]
        return helper(nodes_val)


sol = Solution()
print(len(sol.generateTrees(3)) == 5)
print(len(sol.generateTrees(1)) == 1)
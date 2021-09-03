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
        def build_trees(start, end):
            if start > end:
                return [None]

            trees = []

            for i in range(start, end + 1):
                left_subtrees = build_trees(start, i - 1)
                right_subtrees = build_trees(i + 1, end)
                
                for (left, right) in itertools.product(left_subtrees, right_subtrees):
                    root = TreeNode(i, left, right)
                    trees.append(root)
            return trees

        return build_trees(1, n)

sol = Solution()
print(len(sol.generateTrees(3)) == 5)
print(len(sol.generateTrees(1)) == 1)
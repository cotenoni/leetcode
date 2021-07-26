class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        level = [root]

        while level:
            for i, node in enumerate(level):
                if i < len(level) - 1:
                    node.next = level[i + 1]
            
            level = [child for node in level for child in (node.left, node.right) if child]

        return root



solution = Solution()
tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(6)))
ans = solution.connect(tree)
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        first = True
        result = "["
        queue = collections.deque([root])

        while queue:
            current = queue.popleft()

            if first:
                first = False
            else:
                result += ","
            
            if current:
                result += str(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result += "null"

        result += "]"
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] != "[" or data[-1] != "]":
            raise RuntimeError('Invalid input.')
        data = data[1:len(data) - 1]
        values = data.split(",")

        if not values:
            raise RuntimeError('Invalid input.')

        nodes = [None if node == "null" else TreeNode(int(node)) for node in values]
        candidate_children = nodes[::-1]
        root = candidate_children.pop()

        for node in nodes:
            if node:
                if candidate_children:
                    node.left = candidate_children.pop()
                    
                if candidate_children:
                    node.right = candidate_children.pop()
                  
        return root
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

root = TreeNode(1, TreeNode(2, TreeNode(10)), TreeNode(3, TreeNode(4), TreeNode(5)))
print(ser.serialize(root))
print(deser.deserialize(ser.serialize(root)))

# print(ser.serialize(None))
# print(deser.deserialize(ser.serialize(None)))

# root = TreeNode(1)
# print(ser.serialize(root))
# print(deser.deserialize(ser.serialize(root)))

# root = TreeNode(1, TreeNode(2))
# print(ser.serialize(root))
# print(deser.deserialize(ser.serialize(root)))
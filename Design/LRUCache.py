from typing import Dict

#https://leetcode.com/explore/interview/card/top-interview-questions-hard/122/design/867/
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node()
        self.tail = Node()

        self.head.previous = self.tail
        self.head.next = self.tail
        self.tail.next = self.head
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        value = -1

        if key in self.hash:
            node = self.hash[key]
            value = node.value
            self.removeNode(node)
            self.addNode(node)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.value = value 
            self.removeNode(node)
            self.addNode(node)
        else:
            node = Node(key, value)
            if len(self.hash) == self.capacity:
                nodeToRemove = self.tail.previous
                del self.hash[nodeToRemove.key]
                self.removeNode(nodeToRemove)
            
            self.hash[key] = node
            self.addNode(node)

    def addNode(self, node: Node):
        head_next = self.head.next
        head_next.previous = node

        node.next = head_next
        node.previous = self.head
        self.head.next = node

    def removeNode(self, node: Node):
        node_next = node.next
        node_previous = node.previous

        node_previous.next = node_next
        node_next.previous = node_previous

        

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1)) # 1
obj.put(3, 3)
print(obj.get(2)) # -1
obj.put(4, 4)
print(obj.get(1)) # -1
print(obj.get(3)) # 3
print(obj.get(4)) # 4
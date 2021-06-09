#https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
class MinStackNode:
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        min_value = val

        if len(self.stack) > 0:
            top_element = self.stack[len(self.stack) - 1]

            if top_element.min_value <= val:
                min_value = top_element.min_value

        new_element = MinStackNode(val, min_value)
        self.stack.append(new_element)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1].value

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1].min_value


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.push(2)
obj.push(6)
obj.pop()
print(obj.top())
print(obj.getMin())
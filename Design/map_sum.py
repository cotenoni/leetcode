import collections

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        def default_value():
            return 0

        self._dict = {}
        self._sum_dict = collections.defaultdict(default_value)

    def insert(self, key: str, val: int) -> None:
        old_value = 0
        if key in self._dict:
            old_value = self._dict[key]
            
        self._dict[key] = val
        for i in range(len(key)):
            self._sum_dict[key[:i + 1]] = self._sum_dict[key[:i + 1]] - old_value + val
       
    def sum(self, prefix: str) -> int:
        if prefix in self._sum_dict:
            return self._sum_dict[prefix]
        
        return 0


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
print(obj.insert("apple", 3)) #None
print(obj.sum("ap")) #3
print(obj.insert("app", 2)) #None
print(obj.sum("ap")) #5
print(obj.insert("apple", 5)) #5
print(obj.insert("apple", 1)) #5
print(obj.sum("apple")) #1

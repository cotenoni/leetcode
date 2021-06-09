from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.originalArray = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.originalArray

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        newArray = self.originalArray.copy()
        random.shuffle(newArray)

        return newArray


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())

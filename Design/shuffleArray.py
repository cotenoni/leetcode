from hashlib import new
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original_array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        new_array = self.original_array.copy()
        
        for i in range(len(new_array)):
            random_idx = random.randrange(i, len(new_array))
            new_array[i], new_array[random_idx] = new_array[random_idx], new_array[i]

        return new_array


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.shuffle())

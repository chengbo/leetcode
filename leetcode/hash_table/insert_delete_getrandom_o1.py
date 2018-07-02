import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict.keys():
            return False
        self.nums.append(val)
        self.dict[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict.keys():
            return False
        position = self.dict[val]
        last = len(self.nums) - 1
        self.nums[position] = self.nums[last]
        self.dict[self.nums[last]] = position
        self.nums.pop()
        self.dict.pop(val)
        return True

    def get_random(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        position = random.randint(0, len(self.nums) - 1)
        return self.nums[position]

import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hold_me = []
        self.positions = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self.positions:
            self.hold_me.append(val)
            self.positions[val] = len(self.hold_me) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val in self.positions:
            val_index = self.positions[val]
            last_value = self.hold_me[-1]

            self.hold_me[val_index] = last_value
            self.positions[last_value] = val_index

            self.hold_me.pop()
            del self.positions[val]

            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.hold_me[random.randint(0, len(self.hold_me) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

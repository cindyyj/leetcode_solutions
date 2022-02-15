import random

class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.list = []        

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.pos:
            last, idx = self.list[-1], self.pos[val]
            self.list[idx], self.pos[last] = last, idx
            
            # delete last element
            self.list.pop()
            del self.pos[val]
            return True
        return False
            

    def getRandom(self) -> int:
        return random.choice(self.list)
    
"""
Hashmap provides Insert and Delete in average constant time, although has problems with GetRandom.
Array List has indexes and could provide Insert and GetRandom in average constant time, though has problems with Delete.
To delete a value at arbitrary index takes linear time. The solution here is to always delete the last value:

    Swap the element to delete with the last one.
    Pop the last element out.

For that, one has to compute an index of each element in constant time, and hence needs a hashmap which stores element -> its index dictionary.

Both ways converge into the same combination of data structures:

    Hashmap element -> its index.
    Array List of elements.
"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
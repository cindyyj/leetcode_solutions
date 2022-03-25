# 在 Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict
"""
Time complexity : O(1) both for put and get since all operations with ordered dictionary
    get/in/set/move_to_end/popitem (get/containsKey/put/remove) are done in a constant time.
Space complexity : O(capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.

O(1) time for 
    Get the key / Check if the key exists
    Put the key
    Delete the first added key
    
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.    
"""
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
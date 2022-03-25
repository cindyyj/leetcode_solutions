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

class LRUCache():
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
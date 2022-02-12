
class MyHashMap:
    # Hash + chaining
    def __init__(self):
        self.buckets =  1000
        # The alternative, [{}] * n creates a list of length n with only one dictionary, referenced n times. 
        # This leads to nasty surprises when adding keys to the dictionary.
        self.data = [{} for _ in range(self.buckets) ]
        
    def hash(self, key):
        return key % self.buckets
        
    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        # update if exist
        if key in self.data[hashkey]:
            self.data[hashkey][key] = value
        
        # no add(), append(), or insert() method you can use to add an item to a dictionary in Python
        self.data[hashkey][key] = value
        
    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        # if not exist
        if key not in self.data[hashkey]:
            return -1 
        return self.data[hashkey][key]
        
    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        # if not exist
        if key not in self.data[hashkey]:
            return -1 
        del self.data[hashkey][key]
        
        

# class MyHashMap:
#     # Brute Force
#     def __init__(self):
#         N = 1000001
#         self.data = [-1] * N
        
#     def put(self, key: int, value: int) -> None:
#         self.data[key] = value
        
#     def get(self, key: int) -> int:
#         return self.data[key] if self.data[key] != -1 else -1 

#     def remove(self, key: int) -> None:
#         self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
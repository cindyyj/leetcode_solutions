class TwoSum:

    def __init__(self):
        self.array = []

    def add(self, number: int) -> None:
        self.array.append(number)
        
    def find(self, value: int) -> bool:
        
        sorted_array = sorted(self.array)
        n = len(self.array)
        
        low, high = 0, n - 1
        while low < high:
            total = sorted_array[low] + sorted_array[high]
            if total < value:
                low += 1
            elif total > value:
                high -= 1
            else: 
                return True
        
        return False
"""
how to optimize hashset solution
The following comments refer to this previous solution, but are still relevant:

As I wrote previously, test order matters. For example, switching the order to
(value - num != num or ctr[num] > 1) and value - num in ctr
makes me get TLE consistently.
collections.Counter would be a more obvious choice, but collections.defaultdict is faster. Using Counter, I consistently get TLE.
I don't shortcut ctr = self.ctr just to make the rest prettier but also to make it faster. Looks like that saves ~70 ms on average.
You can see in my new even faster solution I did a few more changes, which all helped.

I also recommend Guido van Rossum's essay about optimization, which includes the local variable optimization. Even Guido himself got surprised at one point :-)

https://leetcode.com/problems/two-sum-iii-data-structure-design/discuss/52034/Fast-and-simple-AC-Python
"""        


# class TwoSum:

#     def __init__(self):
#         self.cache = defaultdict(int)

#     def add(self, number: int) -> None:
#         self.cache[number] += 1

#     def find(self, value: int) -> bool:
#         for num in self.cache:
#             complement = value - num
#             if complement in self.cache:
#                 if complement != num or (complement == num and self.cache[num] >= 2):
#                     return True
#         return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


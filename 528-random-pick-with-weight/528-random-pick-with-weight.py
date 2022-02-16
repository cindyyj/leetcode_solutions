# class Solution:
#     def __init__(self, w):
#         self.w = w

#     def pickIndex(self):
#         # random.choices return a list!
#         return random.choices(range(len(self.w)), weights=self.w)[0]

import random

class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
        
"""
sampling with weight
sampling important step for building decision tree model 

- random.random(): Return random number between 0.0 and 1.0:
- random.choices(): returns a list with the randomly selected element from the specified sequence. Can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
- 


"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
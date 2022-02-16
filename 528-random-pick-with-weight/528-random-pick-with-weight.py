class Solution:
    def __init__(self, w):
        self.w = w

    def pickIndex(self):
        return random.choices(range(len(self.w)), weights=self.w)[0]

# class Solution:

#     def __init__(self, w: List[int]):
#         self.prefix_sums = []
#         prefix_sum =0
#         for weight in w:
#             prefix_sum += weight
#             self.prefix_sums.append(prefix_sum)
        
#         self.total_sum = prefix_sum

#     def pickIndex(self) -> int:
        
"""
sampling with weight
sampling important step for building decision tree model 
"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
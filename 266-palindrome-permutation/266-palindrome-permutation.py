class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        
        counts = collections.Counter(s)
        odds = [cnt for cnt in counts.values() if cnt & 1]  # num & 1 same as num % 2 == 1
        
        return len(odds) <= 1
        
        
        
        
# # --------------------------- METHOD 1 ---------------------------        
#         counts = collections.Counter(s)
#         nums = counts.values()
        
#         odds = even = 0
#         for num in nums:
#             if num & 1:
#                 odds += 1
#             else:
#                 even += 1
        
#         return odds <= 1
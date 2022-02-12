class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # fancy one liner solution as shared by Stefan Pochmann.
        return max(list(map(len, ''.join(map(str, nums)).split('0') )))
#         maxlen = 0
#         start = end = 0

#         while end < len(nums):
#             if nums[end] == 0:
#                 start = end
#                 end += 1
#             while nums[end] == 1:
#                 maxlen = max(maxlen, end - start + 1)
#                 end += 1
        
#         return maxlen
        
        
        
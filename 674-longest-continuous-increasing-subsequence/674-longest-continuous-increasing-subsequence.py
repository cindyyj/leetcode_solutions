class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # sliding window, moving start
        
        if len(nums) <= 1:
            return len(nums)
        
        start = 0
        maxl = 1
        for end in range(1, len(nums)):
            if nums[end] <= nums[end - 1]:
                start = end
            else:
                maxl = max(maxl, end - start + 1)
        
        return maxl 
        
#         # sliding window
#         if len(nums) <= 1:
#             return len(nums)
        
#         maxl = l = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 l += 1
#                 maxl = max(maxl, l)
#             else:
#                 l = 1
                
#         return maxl
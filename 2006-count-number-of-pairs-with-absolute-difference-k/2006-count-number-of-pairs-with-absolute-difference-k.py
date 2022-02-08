from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        # hashmap + dict
        seen = defaultdict(int)
        
        res = 0
        
        for i in range(len(nums)):
            if (nums[i] - k) in seen:
                res += seen[nums[i] - k]
            if (nums[i] + k) in seen:
                res += seen[nums[i] + k]
            
            seen[nums[i]] += 1
        
        return res
            
#         # brute force
#         res, n = 0, len(nums)
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 if abs(nums[j] - nums[i]) == k:
#                     res += 1
        
#         return res
        
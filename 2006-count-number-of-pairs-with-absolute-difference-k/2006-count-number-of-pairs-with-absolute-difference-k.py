from collections import defaultdict

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        # nice usage of defaultdict
        # https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/discuss/1471015/Python-Clean-and-concise.-Dictionary-T.C-O(N)        
        
        seen = defaultdict(int)
        res = 0
        
        for num in nums:
            # if such key doesn't exist, return 0
            res += seen[num - k] + seen[num + k]
            seen[num] += 1
        
        return res

#         # hashmap + dict
#         seen = defaultdict(int)
        
#         res = 0
        
#         for i in range(len(nums)):
#             if (nums[i] - k) in seen:
#                 res += seen[nums[i] - k]
#             if (nums[i] + k) in seen:
#                 res += seen[nums[i] + k]
            
#             seen[nums[i]] += 1
        
#         return res
            
#         # brute force
#         res, n = 0, len(nums)
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 if abs(nums[j] - nums[i]) == k:
#                     res += 1
        
#         return res
        
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter(nums)
        
        for num in counter:
            if k > 0 and num + k in counter:
                res += 1
            elif k == 0 and counter[num] >= 2:
                res += 1
        
        return res
        
        
#         res = set()
#         seen = set()
        
#         for num in nums:
#             if num - k in seen:
#                 res.add((num - k, num))
#             if num + k in seen:
#                 res.add((num, num + k))
                
#             seen.add(num)
            
#         return len(res)
                
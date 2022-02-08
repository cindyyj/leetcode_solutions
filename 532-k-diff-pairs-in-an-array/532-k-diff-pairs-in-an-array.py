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
    
# Explanation
# Count the elements with Counter
# If k > 0, for each element i, check if i + k exist.
# If k == 0, for each element i, check if count[i] > 1


# Explanation
# Time O(N)
# Space O(N)
# https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100135/JavaPython-Easy-Understood-Solution
        
#         res = set()
#         seen = set()
        
#         for num in nums:
#             if num - k in seen:
#                 res.add((num - k, num))
#             if num + k in seen:
#                 res.add((num, num + k))
                
#             seen.add(num)
            
#         return len(res)
                
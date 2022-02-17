from collections import Counter
from itertools import accumulate

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pres = list(accumulate(nums))
        d = Counter()
        d[0] = 1
        cnt = 0
        
        for pre in pres:
            if pre - goal in d:
                cnt += d[pre - goal]
            d[pre] += 1
        
        return cnt
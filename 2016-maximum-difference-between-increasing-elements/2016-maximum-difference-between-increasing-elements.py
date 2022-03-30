class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # The only difference from 121. Best Time to Buy and Sell Stock is that we need to return -1 if no profit can be made.
        
        diff, mi = -1, math.inf
        for i, n in enumerate(nums):
            if i > 0 and n > mi:
                diff = max(diff, n - mi)    
            mi = min(mi, n)
        return diff    
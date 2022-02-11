from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        maxsum = 0
        start = 0
        d = defaultdict(int) 
        total = 0
        
        for end in range(len(nums)):
            total += nums[end]
            d[nums[end]] += 1
            
            while d[nums[end]] > 1:
                d[nums[start]] -= 1
                total -= nums[start]
                start += 1
                
            maxsum = max(maxsum, total)
        
        return maxsum              
            
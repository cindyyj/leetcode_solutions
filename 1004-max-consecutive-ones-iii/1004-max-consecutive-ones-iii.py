from collections import defaultdict

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen, d = 0, defaultdict(int)
        
        start = 0
        for end, num in enumerate(nums):
            d[num] += 1
            
            if d[0] <= k:
                maxlen = max(maxlen, end - start + 1)
            
            while d[0] > k:
                d[nums[start]] -= 1
                start += 1
        
        return maxlen
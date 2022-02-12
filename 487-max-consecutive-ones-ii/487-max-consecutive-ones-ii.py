from collections import defaultdict
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxlen = 0
        d = defaultdict(int)
        
        start = 0
        for end, num in enumerate(nums):
            d[num] += 1
            
            if d[0] <= 1:
                maxlen = max(maxlen, end - start + 1)
            
            while d[0] > 1:
                d[nums[start]] -= 1
                start += 1
            
        return maxlen
            
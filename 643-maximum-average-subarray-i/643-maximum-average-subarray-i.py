class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total, maxavg = 0, float('-inf')
        
        start = 0 
        for end in range(len(nums)):
            total += nums[end]
            if end - start + 1 == k:
                maxavg = max(maxavg, total/k)
            
            if end >= k - 1:
                total -= nums[start]
                start += 1
            
        return maxavg                
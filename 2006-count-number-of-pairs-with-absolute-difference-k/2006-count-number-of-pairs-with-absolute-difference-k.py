class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        # brute force
        res, n = 0, len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if abs(nums[j] - nums[i]) == k:
                    res += 1
        
        return res
        
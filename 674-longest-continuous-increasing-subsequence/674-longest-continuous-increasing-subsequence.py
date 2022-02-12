class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        maxl = l = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                l += 1
                maxl = max(maxl, l)
            else:
                l = 1
                
        return maxl
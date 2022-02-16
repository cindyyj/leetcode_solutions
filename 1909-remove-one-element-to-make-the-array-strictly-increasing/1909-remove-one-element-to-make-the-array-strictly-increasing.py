class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        idx = -1
        cnt = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                idx = i
                cnt += 1
        
        if cnt == 0:
            return True
        
        if cnt == 1:
            if idx == 0 or idx == n - 2:
                return True
            elif nums[idx - 1] < nums[idx + 1] or (idx + 2 < n and nums[idx] < nums[idx + 2]):
                return True
        
        return False
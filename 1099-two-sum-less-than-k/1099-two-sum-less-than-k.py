class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, r = 0, len(nums) - 1
        maxsum = -1

        while l < r:
            total = nums[l] + nums[r]
            if total < k:
                maxsum = max(maxsum, total)
                l += 1
            else:
                r -= 1
        
        return maxsum
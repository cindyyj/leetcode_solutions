class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # return nums.count(target) > len(nums) / 2
        
        """
        bisect_left returns the largest index to insert the element w.r.t. <
        bisect_right returns the largest index to insert the element w.r.t. <=
        """
        n = len(nums)
        if nums[n // 2] != target:
            return False
        
        low = bisect.bisect_left(nums, target)
        high = bisect.bisect_right(nums, target)
        
        return high - low > n / 2
        
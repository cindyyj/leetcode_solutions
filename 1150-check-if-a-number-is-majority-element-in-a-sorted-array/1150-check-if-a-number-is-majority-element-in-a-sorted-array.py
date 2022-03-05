class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # return nums.count(target) > len(nums) / 2
        
#         """
#         bisect_left returns the largest index to insert the element w.r.t. <
#         bisect_right returns the largest index to insert the element w.r.t. <=
#         """
#         n = len(nums)
#         if nums[n // 2] != target:
#             return False
        
#         low = bisect.bisect_left(nums, target)
#         high = bisect.bisect_right(nums, target)
        
#         return high - low > n / 2
        
        
        # smart binary search!
        n = len(nums)
        if nums[n // 2] != target:
            return False
        
        l = 0 
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1 
            else:
                r = mid - 1
                
        try:
            return nums[l + n//2] == target
        except IndexError:
            return False
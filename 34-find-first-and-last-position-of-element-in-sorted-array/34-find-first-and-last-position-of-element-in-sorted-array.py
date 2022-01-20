class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # empty nums
        if not nums:
            return [-1, -1]
        
        def left_bound(nums, target):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = l + (r-l) // 2                
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return l
        
        def right_bound(nums, target):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return r 
        
        start, end = left_bound(nums, target), right_bound(nums, target)
        return [start, end] if start <= end else [-1, -1]
        
        
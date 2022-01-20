class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-w1h4/
        # empty nums
        if not nums:
            return [-1, -1]
        
        # boundry cases
        if target < nums[0] or target > nums[-1]:
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
        
        l = left_bound(nums, target)
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        
        r = left_bound(nums, target + 1)
        return [l, r-1]
        
        
#         # empty nums
#         if not nums:
#             return [-1, -1]
        
#         # boundry cases
#         if target < nums[0] or target > nums[-1]:
#             return [-1, -1]
        
#         def left_bound(nums, target):
#             l, r = 0, len(nums) - 1
            
#             while l <= r:
#                 mid = l + (r-l) // 2                
#                 if nums[mid] < target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
            
#             return l
        
#         def right_bound(nums, target):
#             l, r = 0, len(nums) - 1
            
#             while l <= r:
#                 mid = l + (r-l) // 2
#                 if nums[mid] <= target:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
            
#             return r 
        
#         start, end = left_bound(nums, target), right_bound(nums, target)
#         return [start, end] if start <= end else [-1, -1]
        
        
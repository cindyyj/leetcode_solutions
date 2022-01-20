class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid 
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1 
                else: 
                    l = mid + 1
            
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1 

        
#         # https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/yi-wen-dai-ni-shua-bian-er-fen-cha-zhao-dtadq/
        
#         if not nums:
#             return -1 
        
#         if len(nums) == 1:
#             return 0 if nums[0] == target else -1
        
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = l + (r - l) // 2
            
#             if nums[mid] == target:
#                 return mid
            
#             # 落在同一数组的情况，同时落在数组1 或 数组2
#             if nums[l] <= nums[mid]:
#                 # target 落在 left 和 mid 之间，则移动我们的right，完全有序的一个区间内查找
#                 if nums[l] <= target < nums[mid]:
#                     r = mid - 1
#                 # target 落在right和 mid 之间，有可能在数组1， 也有可能在数组2
#                 elif nums[l] > target or target > nums[mid]:
#                     l = mid + 1
            
#             # 不落在同一数组的情况，left 在数组1， mid 落在 数组2
#             elif nums[l] > nums[mid]:
#                 # 有序的一段区间，target 在 mid 和 right 之间
#                 if nums[mid] < target <= nums[r]:
#                     l = mid + 1
#                 # 两种情况，target 在left 和 mid 之间
#                 elif nums[mid] > target or target > nums[r]:
#                     r = mid - 1
     
        
        # # one-liner, O(n)
        # return nums.index(target) if target in nums else -1
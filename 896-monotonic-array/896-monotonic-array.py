class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc, desc = True, True
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                desc = False
            elif nums[i] > nums[i + 1]:
                inc = False
            
            if not inc and not desc:
                return False
            
        return True
        
        
        
        # return sorted(nums) in [nums, nums[::-1]]
        
#         return all([nums[i] >= nums[i + 1] for i in range(len(nums) - 1)]) or \
#                all([nums[i] <= nums[i + 1] for i in range(len(nums) - 1)])
                
        
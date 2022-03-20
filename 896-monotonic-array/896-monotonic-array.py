class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        return sorted(nums) in [nums, nums[::-1]]
        
#         return all([nums[i] >= nums[i + 1] for i in range(len(nums) - 1)]) or \
#                all([nums[i] <= nums[i + 1] for i in range(len(nums) - 1)])
                
        
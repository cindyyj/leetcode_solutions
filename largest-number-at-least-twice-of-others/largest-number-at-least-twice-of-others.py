class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        else:
            largest = max(nums)
            
            if sorted(nums)[-2] *2 <= largest:
                return nums.index(largest)
            else: 
                return -1      
        
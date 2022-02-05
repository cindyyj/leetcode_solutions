class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        even_idx, odd_idx = 0, 1
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[even_idx] = nums[i]
                even_idx += 2
            else:
                res[odd_idx] = nums[i]
                odd_idx += 2
                
        return res
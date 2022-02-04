class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        
        if zero_count == 1:
            # product
            p = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    idx = i 
                else:
                    p *= nums[i]
            res = [0] * len(nums)
            res[idx] = p
            return res 
            
        if zero_count == 0:
            p = 1
            for i in range(len(nums)):
                p *= nums[i]
            return [p//num for num in nums]
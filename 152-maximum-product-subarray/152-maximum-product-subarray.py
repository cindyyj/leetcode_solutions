class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation
        # save max_prod and min_prod
        # Time O(n), Space O(1)
        
        for i, num in enumerate(nums):
            if i == 0:
                max_prod = min_prod = ans = nums[i]
            else:
                x = max(nums[i], nums[i]*max_prod, nums[i]*min_prod)
                y = min(nums[i], nums[i]*max_prod, nums[i]*min_prod)
                max_prod, min_prod = x, y
                
                # this two line is wrong, as the updated max_prod is used to cal min_prod!!! 
                # max_prod = max(nums[i], nums[i]*max_prod, nums[i]*min_prod)
                # min_prod = min(nums[i], nums[i]*max_prod, nums[i]*min_prod)
            
            ans = max(max_prod, ans)
        
        return ans
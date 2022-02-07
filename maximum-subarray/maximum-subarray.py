class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # classic dp
        
# # To save space, implementation without using DP table
# # At each index, keep track of the maximum sum using variable (max_sum_until_i, and max_sum_sofar)
# # max_until_i = max (max_until_i, max_until_i+cur_value)
# # max_sum_sofar = max(max_until_i, max_sum_sofar,cur_value)
# # Finally, return the max_sum_sofar
# # time O(n)
# # space O(1)        
#         cur_max = glo_max = nums[0]
        
#         for num in nums[1:]:
#             cur_max = max(cur_max + num, num)
#             glo_max = max(cur_max, glo_max)
            
#         return glo_max
        
# https://leetcode.com/problems/maximum-subarray/discuss/898915/Python-easy-solution-with-explanation-(two-approaches-DP-with-and-without-table)
        # At each index, keep track of the maximum sum using DP table , till that point
        # Save the maximum between [cur_value, max_so_far+cur_value]
        # Finally, return the maximum out of the table
        # time O(n)
        # space O(n) 

        dp = [0] * len(nums)
                
        for i, num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)
        
        return max(dp)
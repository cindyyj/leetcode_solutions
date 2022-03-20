class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:    
        
        ans = []
        nums.append(upper + 1)
        prev = lower - 1
        for num in nums:
            diff = num - prev
            if diff == 2:
                ans.append(str(prev + 1))
            elif diff > 2:
                ans.append(f"{prev + 1}->{num - 1}")   
            prev = num    
            
        return ans
        
            
#         #     nums.insert(0,lower-1), nums.append(upper+1)
#         nums = [lower-1] + nums + [upper+1]
#         ans = []
#         for lower, upper in zip(nums, nums[1:]):
#             if lower + 2 == upper:
#                 ans.append(f"{lower + 1}")
#             elif lower + 2 < upper:
#                 ans.append(f"{lower + 1}->{upper - 1}")
#         return ans
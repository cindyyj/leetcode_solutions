class Solution:
#     def threeSumSmaller(self, nums: List[int], target: int) -> int:
#         if len(nums) < 3:
#             return 0
        
#         nums.sort()
        
#         ans = 0
#         for i in range(len(nums) - 2):
#             j, k = i + 1, len(nums) - 1 
#             while j < k:
#                 total = nums[i] + nums[j] + nums[k]
#                 if total < target:
#                     ans += k - j
#                     j += 1
#                 else:
#                     k -= 1
#         return ans
        
    def threeSumSmaller(self, nums: List[int], target: int) -> int:    
        cnt = 0
        nums.sort()
        for i in range(len(nums) - 2):
            # if nums[i] > target: break # don't add this line! this doesn't work for neg, threeSumSmaller([0,-4,-1,1,-1,2], -5)  
            cnt += self.twoSumSmaller(nums, i, target - nums[i])       
        return cnt
    
    def twoSumSmaller(self, nums, i, target):
        l, r = i + 1, len(nums) - 1
        
        cnt = 0
        while l < r:
            total = nums[l] + nums[r]
            if total >= target:
                r -= 1
            else:
                cnt += r - l
                l += 1
        
        return cnt              

"""
[1, 2, 3, 5, 8]
 ↑        ↑
left    right
Now the pair sum is 1 + 5 =6, which is less than targettarget. How many pairs with one of the index=left that satisfy the condition? You can tell by the difference between right and left which is 3, namely (1,2), (1,3), and (1,5). Therefore, we move leftleft one step to its right.
"""
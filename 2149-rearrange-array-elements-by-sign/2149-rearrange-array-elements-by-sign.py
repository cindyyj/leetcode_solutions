class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # two pointer
        pos_idx = 0
        neg_idx = 1
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos_idx] = nums[i]
                pos_idx += 2
            else:
                res[neg_idx] = nums[i]
                neg_idx += 2     
                
        return res
            

#         # list comprehension
#         pos = [num for num in nums if num > 0]
#         neg = [num for num in nums if num < 0]
        
#         ans = []
#         for i in range(len(pos)):
#             ans.append(pos[i])
#             ans.append(neg[i])
        
#         return ans
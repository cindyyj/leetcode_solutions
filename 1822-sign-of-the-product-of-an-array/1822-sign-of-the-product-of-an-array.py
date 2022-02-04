class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # --------------------------- METHOD 2 ---------------------------
        
#         neg_cnt = 0

#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 return 0
#             elif nums[i] < 0:
#                 neg_cnt += 1
        
#         return [1 if neg_cnt % 2 == 0 else -1][0]
        

        # --------------------------- METHOD 1: simplest ---------------------------
        sign = 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            elif nums[i] < 0:
                sign = - sign

        return sign               
        
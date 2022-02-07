class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for num in nums:
            nums[abs(num)-1] = - abs(nums[abs(num)-1]) # when traverse to the index for num, it could already been flipped as negative. 
        
        # # nums.index(num) doesn't work, in case of multiple duplicates. [1,1,2,2]. index(2) always return the first one!!!
        # return [nums.index(num)+1 for num in nums if num > 0] 
        
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        
        return res
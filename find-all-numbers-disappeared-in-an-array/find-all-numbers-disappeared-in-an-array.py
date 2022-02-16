class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 这题用鸽笼原理实现，由题意可得，1~n的位置表示1~n个笼子，如果出现过，相应的“鸽笼”就会被占掉，我们将数字置为负数表示被占掉了。
        # 最后再遍历一遍，如果“鸽笼”为正数就是没出现的数字。  
        
        for num in nums:
            nums[abs(num)-1] = - abs(nums[abs(num)-1]) # when traverse to the index for num, it could already been flipped as negative. 
        
        # # nums.index(num) doesn't work, in case of multiple duplicates. [1,1,2,2]. index(2) always return the first one!!!
        # return [nums.index(num)+1 for num in nums if num > 0] 
        
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        
        return res
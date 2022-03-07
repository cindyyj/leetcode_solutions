class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # easiest two pointers!
        # 荷兰国旗
        # This is a dutch partitioning problem. 
        
        p0 = p1 = 0 # count 0, and 0+1
        
        for i in range(len(nums)):
            # assign 2 for all
            cur, nums[i] = nums[i], 2
            
            # 设1，统计0或1是因为优先放0,0放完才放1
            if cur == 1 or cur == 0:
                nums[p1] = 1
                p1 += 1
                
            # 置0在置1之后，这是因为优先放0，会有错误的1被0替换掉
            # 没被替换的就是正确的1                        
            if cur == 0:
                nums[p0] = 0
                p0 += 1
            
        return
        
# # 时间复杂度：O(n)，其中 n 是数组 nums 的长度。
# # 空间复杂度：O(1)。      
# # 单指针
#         record = collections.Counter(nums)
#         idx = 0 
        
#         for i in range(3):
#             for _ in range(record[i]):
#                 nums[idx] = i 
#                 idx += 1
        
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = 0
        k = 2 # at most appear k times
        for fast in nums:
            if slow < k or nums[slow - k] != fast:
                nums[slow] = fast
                slow += 1
        
        return slow
    
    
#         n = len(nums)
#         if n <= 2:
#             return n
        
#         slow = fast = 2
#         while fast < n:
#             if nums[slow - 2] != nums[fast]:
#                 nums[slow] = nums[fast]
#                 slow += 1
#             fast += 1
        
#         return slow
        
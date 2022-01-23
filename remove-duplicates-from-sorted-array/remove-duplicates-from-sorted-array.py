class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time complextiy : O(n). Assume that nn is the length of array. Each of ii and jj traverses at most nn steps.
        # Space complexity : O(1).
        
        if not nums:
            return 0
        
        slow, fast = 0, 1
        while fast < len(nums): 
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]               
            fast += 1
            
        return slow+1 
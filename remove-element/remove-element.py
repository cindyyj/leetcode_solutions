class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums[:] = [elem for elem in nums if elem != val]
        # return len(nums)
        
        # Time complexity : O(n). Assume the array has a total of nn elements, both i and j traverse at most n steps.
        # Space complexity : O(1).
        if not nums:
            return 0
        
        slow = fast = 0
        
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        
        return slow
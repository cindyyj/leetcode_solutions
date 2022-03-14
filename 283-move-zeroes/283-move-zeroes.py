class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # // If the current element is not 0, then we need to
        # // append it just in front of last non 0 element we found. 
        # // After we have finished processing new elements,
        # // all the non-zero elements are already at beginning of array.
        # // We just need to fill remaining array with 0's.                  
        """
        # S: O(1), T: O(n)  
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
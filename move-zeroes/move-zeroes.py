class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # S: O(1), T: O(n)  
        
        slow = fast = 0
    # // If the current element is not 0, then we need to
    # // append it just in front of last non 0 element we found. 
    
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                
 	# // After we have finished processing new elements,
 	# // all the non-zero elements are already at beginning of array.
 	# // We just need to fill remaining array with 0's.        
    
        for i in range(slow, len(nums)):
            nums[i] = 0
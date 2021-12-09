from math import log10, floor

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        """
        Very common formula for return the number of digits
        in a positive integer. Since we're guranteed there
        are only positive numbers in the array, this works well. If
        negative numbers were allowed, then use log10(abs(num)) instead. 
        """
        count = 0
        
        for num in nums:
            digit_count = floor(log10(num))+1
            if digit_count % 2 == 0:
                count += 1
        
        return count
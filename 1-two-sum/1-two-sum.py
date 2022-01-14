class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time complexity: O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the lookup time to O(1), the overall time complexity is O(n). 
        #  reduce the lookup time from O(n)O(n) to O(1)O(1) by trading space for speed. A hash table is well suited for this purpose because it supports fast lookup in near constant time. I say "near" because if a collision occurred, a lookup could degenerate to O(n)O(n) time. However, lookup in a hash table should be amortized O(1)O(1) time as long as the hash function was chosen carefully.

        # Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly n elements.    
        
        hashdict = dict()        
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashdict:
                return [hashdict[complement], i]
            hashdict[num] = i
        
        return []

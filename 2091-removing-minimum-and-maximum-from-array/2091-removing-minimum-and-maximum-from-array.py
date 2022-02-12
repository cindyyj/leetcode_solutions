class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        i = nums.index(min(nums)) # delete by either minidx + 1, or n - minidx
        j = nums.index(max(nums)) # delete by either maxidx + 1, or n - maxidx
        
        n = len(nums)
        
        return min(max(i + 1, j + 1), 
                   max(n - i, n - j),
                   i + 1 + n - j, 
                   j + 1 + n - i
                  )

        
        """
        Explanation
        Find index i of the minimum
        Find index j of the maximum

        To remove element A[i],
        we can remove i + 1 elements from front,
        or we can remove n - i elements from back.


        Complexity
        Time O(n)
        Space O(1)
        """
        
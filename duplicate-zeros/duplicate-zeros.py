class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        FREE solution 
        https://leetcode.com/problems/duplicate-zeros/discuss/898225/Python-2-solutions-Easy-to-understand-Time-O(N)-Space-O(1)
        """
        
#         n = len(arr)
#         cntZero = arr.count(0)
#         newLen = n + cntZero # Length of new array if we don't trim up to length `n`
        
#         zeros = [0] * cntZero
#         arr.append(zeros)
        
#         # Copy values from the end to beginning
#         i = n - 1
#         j = newLen - 1
        
#         while j >= 0:
#             arr[j] = arr[i]
#             j -= 1
#             if arr[i] == 0: # Copy twice if arr[i] == 0
#                 arr[j] = arr[i]
#                 j -= 1
#             i -= 1

        n = len(arr)
        cntZero = arr.count(0)
        newLen = n + cntZero # Length of new array if we don't trim up to length `n`
        
        # Let's copy values from the end
        i = n - 1
        j = newLen - 1
        while j >= 0:
            # Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
            if j < n: arr[j] = arr[i]   # if j < n, as changes happen in place            
            j -= 1
            if arr[i] == 0: # Copy twice if arr[i] == 0
                if j < n: arr[j] = arr[i]
                j -= 1
            i -= 1        
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        # change it in-place
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens
        
        i, j, n = 0, 1, len(nums)  # pointer for even misplaced, pointer for odd misplaced
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else: # a[i] % 2 == 1 AND a[j] % 2 == 0
                nums[i], nums[j] = nums[j], nums[i]
        return nums
    
#         # change it using space O(n)
#         even_idx, odd_idx = 0, 1
        
#         res = [0] * len(nums)
#         for i in range(len(nums)):
#             if nums[i] % 2 == 0:
#                 res[even_idx] = nums[i]
#                 even_idx += 2
#             else:
#                 res[odd_idx] = nums[i]
#                 odd_idx += 2
                
#         return res
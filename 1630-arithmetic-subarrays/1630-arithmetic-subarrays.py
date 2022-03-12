class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(arr):
            s, n = set(arr), len(arr)
            if len(s) < n: 
                return len(s) == 1 # all same values
            
            # quotient, remainder
            q, r = divmod( max(arr) - min(arr), n - 1)
            
            # remainder needs to be zero and 
            return not r and all(diff in s for diff in range(min(arr), max(arr), q))
        
        return [check(nums[i : j + 1]) for i, j in zip(l, r)]
    
        
#         self.nums = nums
#         return [self.isArithmetic(i, j) for i, j in zip(l, r)]
        
        
#     def isArithmetic(self, left, right):
#         # best, time O(n), space O(1)
#         arr = self.nums[left : (right + 1)]
#         n = len(arr)
        
#         if n < 2:
#             return False
#         if n == 2:
#             return True
#         gap = (max(arr) - min(arr)) / (n - 1)
        
#         if gap == 0:
#             return True
#         if int(gap) != gap:
#             return False
        
#         for i in range(n):
#             num = min(arr) + i * gap
#             if num not in arr:
#                 return False
                
#         return True
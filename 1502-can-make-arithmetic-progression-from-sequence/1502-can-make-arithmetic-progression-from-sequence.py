class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all([(j - i) == arr[1] - arr[0] for i, j in zip(arr, arr[1:])])

        

#         n = len(arr)
#         if n == 2:
#             return True
        
#         arr.sort()
#         diff = arr[1] - arr[0]
        
#         for i in range(2, n):
#             if arr[i] - arr[i - 1] != diff:
#                 return False
        
#         return True      
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # without sort, one loop, time: O(n), space O(n)
        m = min(arr)
        gap = (max(arr) - min(arr)) / (len(arr) - 1)
        if gap == 0: 
            return True
        s = set(num - min(arr) for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)        
        
        
        
        # # sort, time: O(nlogn)
        # arr.sort()
        # return len(set([arr[i] - arr[i - 1] for i in range(1, len(arr))])) == 1
        # # return all([(j - i) == arr[1] - arr[0] for i, j in zip(arr, arr[1:])])

        

#         n = len(arr)
#         if n == 2:
#             return True
        
#         arr.sort()
#         diff = arr[1] - arr[0]
        
#         for i in range(2, n):
#             if arr[i] - arr[i - 1] != diff:
#                 return False
        
#         return True      
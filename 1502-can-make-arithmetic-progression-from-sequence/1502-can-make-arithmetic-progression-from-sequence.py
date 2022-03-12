class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        # best, O(n) + in-place O(1)
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: return True
        i = 0
        while i < len(arr):
            if arr[i] == m + i * gap:
                i += 1
            else:
                dis = arr[i] - m
                if dis % gap != 0: return False
                pos = int(dis / gap)
                if arr[pos] == arr[i]: return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True        

    
        # # 2. without sort, one loop, time: O(n), space O(n)
        # m = min(arr)
        # gap = (max(arr) - min(arr)) / (len(arr) - 1)
        # if gap == 0: 
        #     return True
        # s = set(num - min(arr) for num in arr)
        # return len(s) == len(arr) and all(diff % gap == 0 for diff in s)        
        
        
        
        # # 3. sort, time: O(nlogn)
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
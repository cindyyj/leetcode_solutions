from itertools import accumulate

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        
        for start, end, inc in updates:
            arr[start] += inc
            if end + 1 < length:
                arr[end + 1] -= inc
        
        total = 0
        for i in range(length):
            total += arr[i]
            arr[i] = total
        return arr
    
        # return list(accumulate(arr))
        
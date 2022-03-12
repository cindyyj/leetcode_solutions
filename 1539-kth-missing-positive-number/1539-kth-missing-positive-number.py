class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i in range(1, len(arr) + k + 1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
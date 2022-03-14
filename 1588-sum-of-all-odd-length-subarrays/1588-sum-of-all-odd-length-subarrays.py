class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        # brute force (AC)
        total = 0
        n = len(arr)
        
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                total += sum(arr[start : start + length])
        
        return total
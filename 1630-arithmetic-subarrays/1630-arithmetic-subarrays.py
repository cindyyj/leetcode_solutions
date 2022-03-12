class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        self.nums = nums
        return [self.isArithmetic(i, j) for i, j in zip(l, r)]
        
        
    def isArithmetic(self, left, right):
        # best, time O(n), space O(1)
        arr = self.nums[left : (right + 1)]
        n = len(arr)
        
        if n < 2:
            return False
        if n == 2:
            return True
        gap = (max(arr) - min(arr)) / (n - 1)
        
        if gap == 0:
            return True
        if int(gap) != gap:
            return False
        
        for i in range(n):
            num = min(arr) + i * gap
            if num not in arr:
                return False
                
        return True
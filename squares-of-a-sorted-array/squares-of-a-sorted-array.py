class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l, r = 0, n - 1
        idx = n - 1 
        res = [0] * n
        
        while idx >= 0:
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r] * nums[r]
                r -= 1
            else:
                square = nums[l] * nums[l]
                l += 1
            res[idx] = square
            idx -= 1
        
        return res
                
        
        
        return sorted([num * num for num in nums])
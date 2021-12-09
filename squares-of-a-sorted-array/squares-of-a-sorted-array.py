class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_sq = [num**2 for num in nums]
        nums_sq.sort()
        
        return nums_sq
        
        
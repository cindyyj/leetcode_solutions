class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # # index method takes O(n) time, so your solution is O(n^2).
        # return [sorted(nums).index(num) for num in nums]
        
        # Here a solution with O(n log n) time complexity:
        idx = {}
        for i, n in enumerate(sorted(nums)):
            if n not in idx:
                idx[n] = i
        return [idx[n] for n in nums]

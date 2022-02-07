class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        record = collections.Counter(nums)
        idx = 0 
        
        for i in range(3):
            for _ in range(record[i]):
                nums[idx] = i 
                idx += 1
        
        
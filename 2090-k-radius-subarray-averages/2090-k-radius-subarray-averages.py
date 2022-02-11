class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # use integer division! 
        n = len(nums)
        if n < 2 * k + 1:
            return [-1] * n
        
        total, avg = 0, [-1] * n
        
        for i in range(2*k + 1):
            total += nums[i]        
        avg[k] = total // (2 * k + 1)
        
        for end in range(k + 1, n - k): 
            total -= nums[end - k - 1]
            total += nums[end + k]
                
            avg[end] = total // (2 * k + 1)

        
        return avg
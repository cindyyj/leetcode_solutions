class Solution:
    def getArray(self, n):
        
        if n == 0:
            return [0]
        
        if n == 1:
            return [0, 1]
        
        if n >= 2:
            nums = [0, 1]
            for i in range(2, n+1):
                if i % 2 ==0: 
                    #  list indices must be integers or slices, not float
                    # need to use floor division !!!
                    nums.append(nums[i//2])  
                else:
                    nums.append(nums[(i-1)//2] + nums[(i+1)//2] )
            
        return nums
        
        
        
    def getMaximumGenerated(self, n: int) -> int:
        return max(self.getArray(n))
        
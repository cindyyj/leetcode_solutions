class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        diff = float('inf')
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < abs(diff):
                    diff = target - s
                
                if s < target:
                    j += 1
                else:
                    k -= 1
                
            if diff == 0:
                    break
                
        return target - diff 
        
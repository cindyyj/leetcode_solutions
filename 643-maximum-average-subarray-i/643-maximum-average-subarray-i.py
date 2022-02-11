class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total, maxavg = 0, float('-inf')
        
        start = 0 
        for end in range(len(nums)):
            total += nums[end]
            if end - start + 1 == k:
                maxavg = max(maxavg, total/k)
            
            if end >= k - 1:
                total -= nums[start]
                start += 1
            
        return maxavg            
    
    # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
    # [滑动窗口真滴简单!] 闪电五连鞭带你秒杀12道中档题 (附详情解析)
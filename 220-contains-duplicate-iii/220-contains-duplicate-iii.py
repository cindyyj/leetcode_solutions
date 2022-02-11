class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0: 
            return False
        
        n = len(nums)
        d = {}
        w = t + 1 # bucket of width t+1
        
        for i in range(n):
            m = nums[i] // w
            
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            
            # 我们每个桶中最多只可能有一个元素，多了我们会直接返回结果
            # now bucket m is empty and no almost duplicate in neighbor buckets
            d[m] = nums[i]
            
            # sliding window of size k
            if i >= k:
                del d[nums[i - k] // w]
                
        return False
        
        """ 
        The idea is like the bucket sort algorithm. 
        Suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1). 
        If there are two item with difference <= t, one of the two will happen:

        (1) the two in the same bucket
        (2) the two in neighbor buckets
        """
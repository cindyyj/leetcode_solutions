class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = set()
        seen = set()
        
        for num in nums:
            if num - k in seen:
                res.add((num - k, num))
            if num + k in seen:
                res.add((num, num + k))
                
            seen.add(num)
            
        return len(res)
                
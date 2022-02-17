class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pres = list(accumulate(nums))
        d = Counter()
        d[0] = 1
        cnt = 0
        
        for pre in pres:
            key = (pre % k + k) % k
            if key in d:
                cnt += d[key]
            d[key] += 1
                
        return cnt      
            
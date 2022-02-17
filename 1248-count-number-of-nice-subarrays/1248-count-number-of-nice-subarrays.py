class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odds = [num % 2 for num in nums]
        pres = list(accumulate(odds))
        d = Counter()
        d[0] = 1
        cnt = 0
        
        for pre in pres:
            if pre - k in d:
                cnt += d[pre - k]
            d[pre] += 1
        
        return cnt        
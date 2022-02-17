class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k. 
        # So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding index i
        # 当前 presum 与 K的关系，余数是几，当被除数为负数时取模结果为负数，需要纠正
        
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
            
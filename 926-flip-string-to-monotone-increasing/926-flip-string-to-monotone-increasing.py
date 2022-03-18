class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cnt0 = s.count('0')
        cnt1 = 0
        res = n - cnt0  # flip all 0 to 1s
        
        # for curr pos, count 1s before and 0 after
        # flip 1s to 0 before idx and flip 0 to 1 after idx
        
        for i in range(n):
            if s[i] == '0':
                cnt0 -= 1
            elif s[i] =='1':
                res = min(res, cnt1 + cnt0)  
                cnt1 += 1
        return res
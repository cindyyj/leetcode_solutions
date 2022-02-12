class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        n = len(diff)
        
        start = 0
        cost = 0
        maxl = 0
        
        for end in range(len(diff)):
            cost += diff[end]
            
            if cost <= maxCost:
                maxl = max(maxl, end - start + 1)
                
            while cost > maxCost:
                cost -= diff[start]
                start += 1
        
        return maxl 
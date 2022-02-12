class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l1 = l0 = 0
        maxl1 = maxl0 = 0 
        
        for num in s:
            if num == '1':
                l1 += 1
                l0 = 0
                maxl1 = max(maxl1, l1)
            elif num == '0':
                l1 = 0
                l0 += 1
                maxl0 = max(maxl0, l0)
        
        return maxl1 > maxl0
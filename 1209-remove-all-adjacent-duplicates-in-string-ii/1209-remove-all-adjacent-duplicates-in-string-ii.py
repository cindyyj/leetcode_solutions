class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # two pointer
        n = len(s)
        if n == 0:
            return ""
        
        count = [0] * n
        i = 0
        res = list(s)
        
        for j in range(n):
            res[i] = s[j]
            
            if i > 0 and res[i - 1] == s[j]:
                count[i] = count[i-1] + 1
            else:
                count[i] = 1
            
            if count[i] == k:
                i -= k
            
            i += 1
        
        return "".join(res[:i])
        


        
        # # recursive, time exceeds
        # # time complexity, o(n), worst O(n*n/k), e.g. ABCCBA, k=2, 3 times recursion
        # for i in range(len(s)):
        #     if i + k <= len(s) and s[i:i + k] == s[i] * k:
        #         return self.removeDuplicates(s[:i] + s[(i + k):], k)           
        # return s
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # key is a parameter for the min() function that specifies the sorting order. 
        # If key=len then check the list or tuple or whatever for the value with smallest length and return that value
        if not strs:
            return ""
        strs.sort()
        a = strs[0]
        b = strs[-1]
        res = ""
        for i in range(len(a)):
            if i >= len(b) or a[i] != b[i]:
                break
            res += a[i]
            
        return res
    
    
#         if not strs:
#             return ""
        
#         shortest = min(strs, key=len)
#         for i, c in enumerate(shortest):
#             for other in strs:
#                 if other[i] != c:
#                     return shortest[:i]
#         return shortest
        
        
        # res = ""
        # for s in zip(*strs):
        #     if len(set(s)) == 1:
        #         res += s[0]
        #     else:
        #         break
        # return res        
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if s == t:
            return False
        
        if abs(len(s) - len(t)) > 1:
            return False
        
        i = 0
        while i < min(len(s), len(t)):
            if s[i] == t[i]:
                i += 1
            else:
                break
        
        return s[i+1:] == t[i+1:] or s[i:] == t[i+1:] or s[i+1:] == t[i:]
                
        
        
#         ns, nt = len(s), len(t)
        
#         if ns > nt:
#             return self.isOneEditDistance(t, s)
        
#         # always ns <= nt
#         if nt - ns > 1:
#             return False
        
#         for i in range(ns):
#             if s[i] != t[i]:
#                 if ns == nt:
#                     return s[i + 1 :] == t[i + 1 :]
#                 else:
#                     return s[i:] == t[i+1 :]
            
#         return ns + 1 == nt
                
class Solution:
    def wordPattern(self, p: str, s: str) -> bool: 
        
        # zip
        s = s.split(' ')
        
        # import to ensure the string length are equal, otherwise fail for "aba" "cat cat cat dog"
        if len(p) != len(s):
            return False
        return len(set(p)) == len(set(s)) == len(set(zip(p,s)))  
        
        
#         # 2 hashmap
#         # p for pattern
#         s = s.split(' ')
        
#         p2s = {}
#         s2p = {}
        
#         if len(p) != len(s):
#             return False
#         if len(set(p)) != len(set(s)): 
#             return False # for the case w = ['dog', 'cat'] and p = 'aa'
        
#         # for char, word in zip(p, s):
#         for i in range(len(s)):
            
#             if s[i] not in s2p and p[i] not in p2s:
#                 p2s[p[i]] = s[i]
#                 s2p[s[i]] = p[i]
            
#             elif p2s.get(p[i]) != s[i] or s2p.get(s[i]) != p[i]:
#                 return False
            
#         return True
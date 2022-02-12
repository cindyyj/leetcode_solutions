from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

# --------------------------- METHOD 3 ---------------------------  
        return list(map(s.find, s)) == list(map(t.find, t))
    
# --------------------------- METHOD 2 ---------------------------  
        # string find() 
        # find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        
# --------------------------- METHOD 1, one liner ---------------------------        
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
        
        # # mistake!!! 可能有重复的字母 "aaabbbba"
        # return sorted(Counter(s).values()) == sorted(Counter(t).values())
        
        # https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc).
        
#     def isIsomorphic(self, s, t):
#         s2t, t2s = {}, {}
#         for i in range(len(s)):
#             if s[i] in s2t and s2t[s[i]] != t[i]:
#                 return False
#             if t[i] in t2s and t2s[t[i]] != s[i]:
#                 return False
#             s2t[s[i]] = t[i]
#             t2s[t[i]] = s[i]
#         return True
    
#     def isIsomorphic1(self, s, t):
#         d1, d2 = {}, {}
#         for i, val in enumerate(s):
#             d1[val] = d1.get(val, []) + [i]
#         for i, val in enumerate(t):
#             d2[val] = d2.get(val, []) + [i]
#         return sorted(d1.values()) == sorted(d2.values())
        
#     def isIsomorphic2(self, s, t):
#         d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
#         for i, val in enumerate(s):
#             d1[ord(val)].append(i)
#         for i, val in enumerate(t):
#             d2[ord(val)].append(i)
#         return sorted(d1) == sorted(d2)
    
#     def isIsomorphic5(self, s, t):
#         return map(s.find, s) == map(t.find, t)

#     def isIsomorphic6(self, s, t):
#         d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
#         for i in xrange(len(s)):
#             if d1[ord(s[i])] != d2[ord(t[i])]:
#                 return False
#             d1[ord(s[i])] = i+1
#             d2[ord(t[i])] = i+1
#         return True
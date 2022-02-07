class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        # stack
        letters = [c for c in s if c.isalpha()]
        
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        
        return ''.join(ans)
        
        
#         # two pointers
#         l, r = 0, len(s) - 1
#         s = list(s)
#         while l < r:
#             if not s[l].isalpha():
#                 l += 1
#             elif not s[r].isalpha():
#                 r -= 1
#             else:
#                 # string doesn't support item assignment!!!
#                 s[l], s[r] = s[r], s[l]
#                 l += 1
#                 r -= 1
                
#         return ''.join(s)
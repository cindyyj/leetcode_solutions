class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        backspace = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(backspace, s, "") == reduce(backspace, t, "")
        
#         def build(s):
#             ans = ""
#             for c in s:
#                 if c != '#':
#                     ans += c
#                 elif ans:
#                     ans = ans[:-1]
#             return ans
        
#         return build(s) == build(t)                
                   
        
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        pair = {
            '(' : ')',
            '[' : ']',
            '{' : '}',    
        }

        stack = list()
        for c in s:
            if c in pair:
                stack.append(c)
            elif c in pair.values():
                if stack and pair[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return stack == []
        
#         if len(s) % 2 != 0:
#             return False
        
#         pairs = {
#             ")" : "(", 
#             "}" : "{", 
#             "]" : "[", 
#         }
        
#         stack = list()
                  
#         for char in s:
#             if char in "({[":
#                 stack.append(char)
#             elif char in "]})":
#                 # 右括号比左括号先出现, 不能闭合 not stack 
#                 # 遇到右括号, 必然要与上一个左括号闭合, 如果不匹配就 False
#                 if not stack or stack[-1] != pairs[char]:
#                     return False
#                 else: 
#                     stack.pop()
                    
#         # 正常闭合的情况下, 栈里面应该全都弹出去了, 所以应该是空的
#         return stack == []
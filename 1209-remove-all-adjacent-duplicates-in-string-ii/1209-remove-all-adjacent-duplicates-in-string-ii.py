class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 2 stack with reconstruction
        # one stack for holding unique elements let's say (stack)
        # another stack (let say counter_stack) for storing current count from the stack.peek( )
        # Loop through each item in s and adjust/remove top elements of both stacks.
        # build a return string using both of the stacks.
        # Simple Python3 implementation is below.
        
        stack = [] # unique char
        counts = [] # counts

        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
                counts.append(1)
            elif stack[-1] == char:
                counts[-1] += 1
            
            if counts[-1] == k:
                stack.pop()
                counts.pop()
        
        return ''.join([stack[i] * counts[i] for i in range(len(stack))])
        
#         # two pointer, time O(n), space O(n)
#         n = len(s)
#         if n == 0:
#             return ""
        
#         count = [0] * n
#         i = 0
#         res = list(s)
        
#         for j in range(n):
#             res[i] = s[j]
            
#             if i > 0 and res[i - 1] == s[j]:
#                 count[i] = count[i-1] + 1
#             else:
#                 count[i] = 1
            
#             if count[i] == k:
#                 i -= k
            
#             i += 1
        
#         return "".join(res[:i])
        


        
        # # recursive, time exceeds
        # # time complexity, o(n), worst O(n*n/k), e.g. ABCCBA, k=2, 3 times recursion
        # for i in range(len(s)):
        #     if i + k <= len(s) and s[i:i + k] == s[i] * k:
        #         return self.removeDuplicates(s[:i] + s[(i + k):], k)           
        # return s
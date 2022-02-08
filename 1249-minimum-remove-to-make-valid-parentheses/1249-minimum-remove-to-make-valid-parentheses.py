class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/solution/yi-chu-wu-xiao-gua-hao-by-leetcode/
        # Convert string to list, 
        # because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
        
        s = list(s)
        stack = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    # if no matching (, remove this unmatched )
                    s[i] =''
        
        while stack:
            i = stack.pop()
            s[i] = ''
        
        return ''.join(s)
        

# # Iterate through list
# # Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
# # When we come across close parenthesis we pop an element from the stack. 
# # If the stack is empty we replace current list element with an empty string
# # After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
# # Convert list to string and return

#         indexes_to_remove = set()
#         stack = []
#         s = list(s)
        
#         for i, c in enumerate(s):
#             if c not in '()':
#                 continue
#             elif c == '(':
#                 stack.append(i)
#             # c == ) and stack not empty
#             elif stack:
#                 stack.pop()
#             # c == ) and stack empty
#             else:
#                 indexes_to_remove.add(i)
            
#         indexes_to_remove = indexes_to_remove.union(stack)

#         string = []
#         for i, c in enumerate(s):
#             if i not in indexes_to_remove:
#                 string.append(c)
            
#         return ''.join(string)
        
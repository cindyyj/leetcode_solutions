class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/solution/yi-chu-wu-xiao-gua-hao-by-leetcode/
        # Convert string to list, 
        # because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
        
        indexes_to_remove = set()
        stack = []
        s = list(s)
        
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            # c == ) and stack not empty
            elif stack:
                stack.pop()
            # c == ) and stack empty
            else:
                indexes_to_remove.add(i)
            
        indexes_to_remove = indexes_to_remove.union(stack)

        string = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string.append(c)
            
        return ''.join(string)
        
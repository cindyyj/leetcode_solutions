class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # Initiate an empty output stack. 
        # Iterate over all characters in the string.
        # Current element is equal to the last element in stack? Pop that last element out of stack.
        # Current element is not equal to the last element in stack? Add the current element into stack.
        # Convert stack into string and return it.
        
        output = []
        for char in s:
            if output and char == output[-1]:
                output.pop()
            else:
                output.append(char)
        return ''.join(output)
        
#         # lowercase, uppercase? 
#         # length of string?
        
#         # wrong answer, fail for the case of mulitple duplicates "abbaca" -> "ca"
#         if len(s) <= 1:
#             return s
        
#         i, j = 0, 1
#         s = list(s)
#         while j < len(s):
#             if s[i] == s[j]:
#                 s[i] = s[j] = ''
#             i += 1
#             j += 1
            
#         return ''.join(s)
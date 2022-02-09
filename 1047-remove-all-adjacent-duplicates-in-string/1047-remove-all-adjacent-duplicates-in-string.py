class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # two pointer
        # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893/JavaC%2B%2BPython-Two-Pointers-and-Stack-Solution
        # You can easily update this solution to remove more duplicates.
        # Now it's a specil case where we only remove replicates k = 2.
        
        # i refers to the index to set next character in the output string.
        # j refers to the index of current iteration in the input string.

        # Iterate characters of S one by one by increasing j.

        # If S[j] is same as the current last character S[i - 1],
        # we remove duplicates by doing i -= 2.

        # If S[j] is different as the current last character S[i - 1],
        # we set S[i] = S[j] and increment i++.
        

        i = j = 0
        res = list(s)
        while j < len(s):
            # 先把original的字符赋值 output
            res[i] = s[j]
            
            # 然后判断左边挨着的两个字符是否相同，如果相同，
            # 他两同时消失，也就是left往回退两步
            
            if (i > 0 and res[i - 1] == res[i]):
                i -= 2
            
            j += 1
            i += 1 #上一个未消除的字母位置，或者-1
        
        return ''.join(res[:i])
        
#         # stack
#         # Initiate an empty output stack. 
#         # Iterate over all characters in the string.
#         # Current element is equal to the last element in stack? Pop that last element out of stack.
#         # Current element is not equal to the last element in stack? Add the current element into stack.
#         # Convert stack into string and return it.
        
#         output = []
#         for char in s:
#             if output and char == output[-1]:
#                 output.pop()
#             else:
#                 output.append(char)
#         return ''.join(output)
    
    
    
        
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
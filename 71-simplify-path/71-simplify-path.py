class Solution:
    def simplifyPath(self, path: str) -> str:

        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str
    
    
#         stack = []
#         for p in path.split('/'):
#             if stack and p == '..':
#                 stack.pop()
#             elif p in ['.', ''] :  # no-op for '.' or empty string (not '' = True)
#                 continue
#             else: # a directory name
#                 stack.append(p)
                
#         return '/' + '/'.join(stack)
        
        
        """
具体的，从前往后处理 path，每次以 item 为单位进行处理（有效的文件名），根据 item 为何值进行分情况讨论：

item 为有效值 ：存入栈中；
item 为 .. ：弹出栈顶元素（若存在）；
item 为 . ：不作处理。

作者：AC_OIer
链接：https://leetcode-cn.com/problems/simplify-path/solution/gong-shui-san-xie-jian-dan-zi-fu-chuan-m-w7xi/

示例 4：
输入：path = "/a/./b/../../c/"
输出："/c"
        """
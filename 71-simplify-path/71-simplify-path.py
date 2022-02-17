class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if stack and p == '..':
                stack.pop()
            elif p not in " ..":
                stack.append(p)
        return '/' + '/'.join(stack)

# 作者：qingfengpython
# 链接：https://leetcode-cn.com/problems/simplify-path/solution/71-jian-hua-lu-jing-biao-zhun-de-zhan-we-0ebf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。   
#         stack = []
#         for p in path.split('/'):
#             if stack and p == '..':
#                 stack.pop()
#             elif p in ['.', ''] :  # no-op for '.' or empty string (not '' = True)
#                 continue
#             else: # a directory name
#                 stack.append(p)
                
# #         return '/' + '/'.join(stack)
        
        
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
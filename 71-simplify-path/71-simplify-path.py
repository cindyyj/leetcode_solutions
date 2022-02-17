class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if stack and p == '..':
                stack.pop()
            elif p not in "..":  # p is not empty, not '.', not '..'
                stack.append(p)
        return '/' + '/'.join(stack)

        
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
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        cur = ""
        
        def backtrack(cur, left, right):
            if len(cur) == 2*n:
                ans.append(cur)
                return 
            if left < n:
                backtrack(cur + "(", left + 1, right) 
            if right < left:
                backtrack(cur +")", left, right + 1)
        
        backtrack(cur, 0, 0)
        return ans
    
        
#         res = []
#         cur_str = ''
        
#         def dfs (cur_str, left, right):
#             """
#             :param cur_str: 从根结点到叶子结点的路径字符串
#             :param left: 左括号还可以使用的个数
#             :param right: 右括号还可以使用的个数
#             :return:
#             """
#             if left == right == 0:
#                 res.append(cur_str)
#                 return 
#             if right < left:
#                 return
#             if left > 0:
#                 dfs(cur_str + "(", left - 1, right)
#             if right > 0:
#                 dfs(cur_str + ")", left, right - 1)
                
#         dfs(cur_str, n, n)
#         return res
            

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/        
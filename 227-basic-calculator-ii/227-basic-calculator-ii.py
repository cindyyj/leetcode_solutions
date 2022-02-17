class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)

# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/xian-cheng-chu-zai-jia-jian-yong-zhan-ba-hplr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#         stack = list()
#         num = 0
#         pre = '+'
        
#         for i, c in enumerate(s):
#             if c.isnumeric():
#                 num = num * 10 + int(c)
#             if c in '+=*/' or i == len(s) - 1:
#                 if pre == '+':
#                     stack.append(num)
#                 elif pre == '-':
#                     stack.append(-num)
#                 elif pre == '*':
#                     stack.append(stack.pop() * num)
#                 else:
#                     stack.append(int( stack.pop() / num)) #「浮点除 / 」再取整
                
#                 pre = c
#                 num = 0
                
#         return sum(stack)

                    
    """
    Python3「地板除 // 」。比如在 Python3 中 (-3) // 2 = -2 的，和 c++ 计算负数除法的结果不一样。因此如果在计算的过程中，如果遇到负数的除法，先使用的用「浮点除 / 」再取整的方式获得和 c++一样的结果

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/xian-cheng-chu-zai-jia-jian-yong-zhan-ba-hplr/
   
    """
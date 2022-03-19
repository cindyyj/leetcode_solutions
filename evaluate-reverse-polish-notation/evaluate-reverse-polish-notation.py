import operator as op

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": add,
            "-": sub,
            "*": mul,
            # `operator.truediv a/b` & `operator.floordiv a//b` are not correct
            # -3 // 2 = -2
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                res = operators[token](num1, num2)     
                stack.append(int(res))
            else:
                stack.append(int(token))
                
        return stack[0]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/solution/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
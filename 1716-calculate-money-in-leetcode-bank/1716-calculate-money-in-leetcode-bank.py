class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = 0, 1
        res = 0
        for i in range(n):
            res += week + day
            day += 1
            if day == 8:
                day = 1
                week += 1
        return res

"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/solution/ji-suan-li-kou-yin-xing-de-qian-by-leetc-xogx/
"""       
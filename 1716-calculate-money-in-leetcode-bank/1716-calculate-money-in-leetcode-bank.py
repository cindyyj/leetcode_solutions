class Solution:
    def totalMoney(self, n: int) -> int:
        # 等差数列求和 arithmetic sequence
        # 所有完整的周存的钱
        weekNumber = n // 7
        firstWeekMoney = (1 + 7) * 7 // 2
        lastWeekMoney = firstWeekMoney + 7 * (weekNumber - 1)
        weekMoney = (firstWeekMoney + lastWeekMoney) * weekNumber // 2
        # 剩下的不能构成一个完整的周的天数里存的钱
        dayNumber = n % 7
        firstDayMoney = 1 + weekNumber
        lastDayMoney = firstDayMoney + dayNumber - 1
        dayMoney = (firstDayMoney + lastDayMoney) * dayNumber // 2
        return weekMoney + dayMoney  
        
        # # simulation
        # week, day = 0, 1
        # res = 0
        # for i in range(n):
        #     res += week + day
        #     day += 1
        #     if day == 8:
        #         day = 1
        #         week += 1
        # return res

"""
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank/solution/ji-suan-li-kou-yin-xing-de-qian-by-leetc-xogx/
"""       
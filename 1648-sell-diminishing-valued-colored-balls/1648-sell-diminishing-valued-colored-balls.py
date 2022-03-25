class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # 用于计算卖出矩形可以获得的价值
        def calc_matrix(u: int, h: int, w: int) -> int:
            return h * (u + u - h + 1) * w // 2

        mod = 10 ** 9 + 7
        # 先排序 inventory，这里插入个零可以避免边界判断
        inventory.append(0)
        inventory.sort()
        self.count = 0
        now = len(inventory) - 1
        width = 1
        while now > 0:
            # 跳过的部分都当前的最大值，都是可以卖的
            while inventory[now - 1] == inventory[now]:
                now -= 1
                width += 1

            upper = inventory[now]
            lower = inventory[now - 1]
            # 可以卖出的数额不足 (upper - lower) * width 这个矩形
            if orders < (upper - lower) * width:
                h = orders // width
                self.count += calc_matrix(upper, h, width) + ((orders - h * width) * (upper - h))
                self.count %= mod
                break
            self.count += calc_matrix(upper, upper - lower, width)
            self.count %= mod
            orders -= (upper - lower) * width
            width += 1
            now -= 1
        return self.count

# 作者：ykousbi-ji
# 链接：https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls/solution/pai-xu-by-ykousbi-ji/     
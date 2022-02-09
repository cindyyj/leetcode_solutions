class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # https://leetcode.com/problems/assign-cookies/discuss/210952/Python3
        
        # 先对g, s两个数组进行排序
        # 贪心算法
        # 贪心思想1 优先满足需求因子较小的孩子。因为如果较小需求的孩子无法被满足，则之后的较大的需求更不可能能被满足了。
        # 贪心思想2 尽量用较小的糖果去优先满足孩子。
        
        g.sort()    # 对需求因子进行排序，从小到大
        s.sort()    # 对糖果数组进行排序，从小到大
        child  = 0  # 记录可以被满足孩子数
        cookie = 0  # 记录可以满足的糖果数
        while  child <len(g) and cookie < len(s):
            if g[child] <= s[cookie]: 
                child += 1
            cookie += 1
        return child
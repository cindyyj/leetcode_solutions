class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # https://leetcode.com/problems/assign-cookies/discuss/210952/Python3
        g.sort()    # 对需求因子进行排序，从小到大
        s.sort()    # 对糖果数组进行排序，从小到大
        child  = 0  # 记录可以被满足孩子数
        cookie = 0  # 记录可以满足的糖果数
        while  child <len(g) and cookie < len(s):
            if g[child] <= s[cookie]: 
                child += 1
            cookie += 1
        return child
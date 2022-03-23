class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        # greedy
        n = len(colors)
        if colors[0] != colors[-1]:
            return n - 1
        
        # 头尾颜色相同
        l, r = 1, n - 2
        while l < n and colors[l] == colors[0]:
            l += 1
        while r >= 0 and colors[r] == colors[0]:
            r -= 1
        return max(r, n - 1 - l)

        
        # # brute force
        # n = len(colors)
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if colors[i] != colors[j]:
        #             res = max(res, j - i)
        # return res        
    
    
    """
    解题思路 此处撰写解题思路

判断首尾
首尾不满足条件同时收缩
判断不同元素到两头的距离
返回较大的值
时间复杂度 o(logn) 空间复杂度 o(1)
    """
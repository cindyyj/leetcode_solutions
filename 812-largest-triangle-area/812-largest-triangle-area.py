class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/largest-triangle-area/solution/zui-da-san-jiao-xing-mian-ji-by-leetcode/
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
      
        # https://en.wikipedia.org/wiki/Shoelace_formula 
        
        def area(p1, p2, p3):
            return 0.5 * abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] 
                          - p1[1] * p2[0] - p2[1] * p3[0] - p3[1] * p1[0])
        
        return max(area(*triangle) 
                  for triangle in itertools.combinations(points, 3))
    """
    有用的求任意简单多边形面积的经典公式。
    所谓“简单多边形”，可以是凹、或凸多边形，但原则上边与边之间不能有交叉；
    或者，拓扑一点，从多边形卷绕数的角度，多边形内的点卷绕数只能是。
    # 作者：LeetCode
    # 链接：https://leetcode-cn.com/problems/largest-triangle-area/solution/zui-da-san-jiao-xing-mian-ji-by-leetcode/
    """

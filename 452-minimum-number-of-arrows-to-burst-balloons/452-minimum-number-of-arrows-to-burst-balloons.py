class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        # sort by end point
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        prev_end = points[0][1]
        
        for start, end in points:
            if prev_end < start:  # xstart and xend is burst by an arrow shot at x if xstart <= x <= xend
                arrows += 1
                prev_end = end
        
        return arrows               
        
        
        """

435, 无重叠区间  本题其实和452.用最少数量的箭引爆气球非常像，弓箭的数量就相当于是非交叉区间的数量，只要把弓箭那道题目代码里射爆气球的判断条件加个等号（认为[0，1][1，2]不是相邻区间），然后用总区间数减去弓箭数量 就是要移除的区间数量了。

作者：carlsun-2
链接：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/435-wu-zhong-die-qu-jian-tan-xin-jing-di-qze0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        当前区间  -----R
          区间a ----------R
             区间b  L--------
     
     如上图，当前区间遇到重合区间 a，a 的右端>=自己的右端（因为右端递增），
     遇到下一个重合区间 b，b 的左端<=自己的右端（因为有重合），所以a、b 一定有交集，参照物是当前区间的右端。

    于是，放心地让当前区间一路找重合，直到遇到不重合，就有了一组能一箭穿的。

    作者：xiao_ben_zhu
    链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/tu-jie-tan-tao-wei-shi-yao-yao-an-qu-jian-de-you-d/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
        """
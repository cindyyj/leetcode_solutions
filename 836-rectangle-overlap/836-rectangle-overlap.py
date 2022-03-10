class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        # https://leetcode-cn.com/problems/rectangle-overlap/solution/tu-jie-jiang-ju-xing-zhong-die-wen-ti-zhuan-hua-we/
        # change 2d overlap to 1d interval overlap
        # only not overlap if 
        # 假设两个区间分别是 [s1, e1] 和 [s2, e2] 的话，区间不重叠的两种情况就是 e1 <= s2 和 e2 <= s1。
        
        x_overlap = not(rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
        y_overlap = not(rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        
        return x_overlap and y_overlap
        
        
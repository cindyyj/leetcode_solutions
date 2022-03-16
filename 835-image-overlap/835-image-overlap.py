class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        我们反向思考方法一，就可以得到一种新的方法。
        我们分别枚举 A 和 B 中的一个 1，计算出偏移量 delta 并放入计数器中。
        对于每一个 delta，如果它在计数器中出现了 k 次，
        那么偏移量为 delta 时，A 和 B 重合的 1 的数目就为 k。

        作者：LeetCode
        链接：https://leetcode-cn.com/problems/image-overlap/solution/tu-xiang-zhong-die-by-leetcode/
        """
        
        n = len(img1)
        cnt = collections.Counter()
        
        for i1, row1 in enumerate(img1):
            for j1, v1 in enumerate(row1):
                if v1:
                    for i2, row2 in enumerate(img2):
                        for j2, v2 in enumerate(row2):
                            if v2:
                                cnt[(i1-i2, j1-j2)] += 1
        return max(cnt.values() or [0])
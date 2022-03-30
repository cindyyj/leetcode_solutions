from heapq import heappush, heappop 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key = lambda x : x[0]**2 + x[1]**2)
        return points[:k]
        
        # # minheap, find the closest to origin
        # queue = []
        # n = len(points)
        # for i in range(n):
        #     heappush(queue, (points[i][0]**2 + points[i][1]**2, points[i]))
        # res = []
        # for i in range(k):
        #     res.append(heappop(queue)[1])
        # return res

        # 作者：jalan
        # 链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/tou-lan-yu-kuai-pai-by-jalan/
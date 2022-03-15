class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # directed graph
        
        indegrees = Counter([y for _, y in trust])
        outdegrees = Counter([x for x, _ in trust])
        
        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i
        return -1
        
        """
        计算各节点的入度和出度
        思路及解法

        题干描述了一个有向图。每个人是图的节点， trust[i] 是图的有向边，从 \textit{trust}[i][0]trust[i][0] 指向 \textit{trust}[i][1]trust[i][1]。我们可以遍历 \textit{trust}trust，统计每个节点的入度和出度，存储在 \textit{inDegrees}inDegrees 和 \textit{outDegrees}outDegrees 中。

        根据题意，在法官存在的情况下，法官不相信任何人，每个人（除了法官外）都信任法官，且只有一名法官。因此法官这个节点的入度是 n-1n−1, 出度是 00。

        我们可以遍历每个节点的入度和出度，如果找到一个符合条件的节点，由于题目保证只有一个法官，我们可以直接返回结果；如果不存在符合条件的点，则返回 -1−1。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/find-the-town-judge/solution/zhao-dao-xiao-zhen-de-fa-guan-by-leetcod-0dcg/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
            
        
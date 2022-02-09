class Solution:
    def candy(self, ratings: List[int]) -> int:
# 代码随想录  那么本题我采用了两次贪心的策略：

# 一次是从左到右遍历，只比较右边孩子评分比左边大的情况。
# 一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
# 这样从局部最优推出了全局最优，即：相邻的孩子中，评分高的孩子获得更多的糖果。

# 作者：carlsun-2
# 链接：https://leetcode-cn.com/problems/candy/solution/dai-ma-sui-xiang-lu-135-fen-fa-tang-guo-f7ezy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。        
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j + 1] + 1, candies[j])
        
        return sum(candies)
        
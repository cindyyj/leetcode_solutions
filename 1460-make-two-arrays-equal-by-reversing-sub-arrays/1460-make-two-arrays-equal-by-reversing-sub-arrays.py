class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return sorted(target) == sorted(arr)
        return collections.Counter(target) == collections.Counter(arr)

        
# 通过样例的启发，就是判断两个数组元素是否相同。
# 证明也很简单，需要知道冒泡排序的过程，如果不知道可以学习一下。
# 冒泡排序的所有操作都是不断交换相邻两个元素的过程，交换相邻两个元素的操作也是反转子数组的一种。
# 考虑数组target，它一定可以通过冒泡排序变成递增（递减）的数组。假设我们记录下每一次的交换，记为操作序列A。
# 考虑数组 arr，它也一定可以通过冒泡排序变成递增（递减）的数组。
# 如果target与arr元素相同，那么最终冒泡排序结果也相同。将数组arr进行冒泡排序，再进行操作序列A的逆过程，就一定可以得到target。
# 如果数组target的元素与数组arr的元素不同，显然无法通过arr得到target。

# 作者：bowen-17
# 链接：https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/solution/kan-zhao-hen-xia-ren-shi-ji-bi-jiao-liang-ge-shu-z/

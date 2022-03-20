class NumArray:
    # 只有在不得不写「线段树」的时候，我们才考虑线段树。
    def __init__(self, nums: List[int]):
        # 初始化sum 数组, 从一计数, 0 号不用, # 从第一个数计算下标和
        # x & (-x) gets the LSB (least significant bit).
        self.tree = [0 for _ in range(len(nums) + 1)]
        for k in range(1, len(self.tree)):
            self.tree[k] = sum(nums[k - (k & -k) : k])

    def update(self, index: int, val: int) -> None:
        # 计算更新的值和原数的差值, i,j从0 计数

        diff = val - self.sumRange(index, index)
        k = index + 1
        while k < len(self.tree):
            self.tree[k] += diff
            k += k & -k
    
    def sumk(self, k: int) -> int:
        res = 0
        while k >= 1:
            res += self.tree[k]
            k -= k & -k 
        return res
        
        
    def sumRange(self, left: int, right: int) -> int:
        
        # i, j are nums index (0-index)
        if left + 1 == 1:
            return self.sumk(right + 1)
        else:
            return self.sumk(right + 1) - self.sumk(left)
            

"""
Binary Indexed Tree. It is faster and simpler to code than Segment Trees

Time, O(logn)
Space, O(1)

x manages the sum in the range [x - x & (-x), x - 1].
So whenever index y gets update, we need to update all indices x such that x - x & (-x) <= y <= x - 1. 
However, I don't know how to solve this in-equation. I know the answer is: y + y & (-y), and continue. But why?

Solving the inequality the you gave is not easy, but you can view in a different angle. 
That is, once an index (of BIT array) [y] is updated, from the tree structure of the BIT (see the meaning of BIT[i] I gave above), you can immediate see that the parent node of [y], which has the index z=y+(y&-y) should be updated, and so is z+(z&-z), and so on and on, until the end of the BIT array.


针对不同的题目，我们有不同的方案可以选择（假设我们有一个数组）：

1. 数组不变，求区间和：「前缀和」、「树状数组」、「线段树」
2. 多次修改某个数，求区间和：「树状数组」、「线段树」
3. 多次整体修改某个区间，求区间和：「线段树」、「树状数组」（看修改区间的数据范围）
4. 多次将某个区间变成同一个数，求区间和：「线段树」、「树状数组」（看修改区间的数据范围）

这样看来，「线段树」能解决的问题是最多的，那我们是不是无论什么情况都写「线段树」呢？

答案并不是，而且恰好相反，只有在我们遇到第 4 类问题，不得不写「线段树」的时候，我们才考虑线段树。

因为「线段树」代码很长，而且常数很大，实际表现不算很好。我们只有在不得不用的时候才考虑「线段树」。

作者：AC_OIer
链接：https://leetcode-cn.com/problems/range-sum-query-mutable/solution/guan-yu-ge-lei-qu-jian-he-wen-ti-ru-he-x-41hv/

前置知识

对数字的二进制表示有认识
最好知道前缀和的原理
对树状数组和线段树的简易区分：

    树状数组只能让整个区间加一个数
    线段树可以让一个区间全部变成一个数也可以让整个区间加一个数，虽然实现更复杂但是更强大

因而有以下常识：

    能用树状数组用树状数组，实在不行再用线段树
    树状数组更快空间消耗也更小，空间复杂度也更低。

本题我们来考虑树状数组，Binary Indexed Tree (Fenwick Tree)

为什么要用树状数组？
    前缀和求和是O(1)，add是O(n)。
    普通数组add是O(1)，求和是O(n)。

因此，我们需要一个更好的方式实行一个平衡。

// 代码来自oi-wiki 下方给了link
int lowbit(int x) { 
  // x 的二进制表示中，最低位的 1 的位置。
  // getlowbit(0b10110000) == 0b00010000
  //          ~~~^~~~~
  // getlowbit(0b11100100) == 0b00000100
  //          ~~~~~^~~
  return x & -x;

把13变换成二进制是 1 1 0 1，去掉最后一位1的话变成12，1 1 0 0。

如果我们再去掉一位呢？变成8，1 0 0 0。

这时候你是不是已经发现了，此时我们的8的二进制表达中，已经只剩下一个1了。而且我们获得了2个很重要的数字。

一个是12（1 1 0 0），一个是8（1 0 0 0），都是通过13（1 1 0 1）去掉1来获得的。这两个数字就是我们之前用来计算[1, 13]的和用到的关键数字。

Sum(13) = Range(1,8) + Range(9,12) + Range(13,13) = 29 + 10 + 4 = 44Sum(13)=Range(1,8)+Range(9,12)+Range(13,13)=29+10+4=44

我们再举一个栗子。

数字7，二进制表达为0 1 1 1。按照惯例我们先去掉第一个1，变成了6，查上表可以得到一个区间和13.

再去掉一个1，变成了4，查上表可以得到一个区间和11。

最后加上坐标7本身的区间和3。

我们可以得到Sum(7) = 13+11+3 = 27Sum(7)=13+11+3=27

作者：onjoujitoki
链接：https://leetcode-cn.com/problems/range-sum-query-mutable/solution/cong-wei-yun-suan-kai-shi-de-shu-zhuang-k6dqb/

"""
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
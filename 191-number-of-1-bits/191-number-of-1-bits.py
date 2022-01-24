class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
        
#         得到二进制字符串，统计字符串中 "1" 的次数即可。
#         需要注意的是，二进制字符串是以 "0b" 开头，所以如果题目要问的是二进制中 0 的个数，需要注意答案是 bin(n).count("0") - 1。

# 作者：fuxuemingzhu
# 链接：https://leetcode-cn.com/problems/number-of-1-bits/solution/fu-xue-ming-zhu-xiang-jie-wei-yun-suan-f-ci7i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
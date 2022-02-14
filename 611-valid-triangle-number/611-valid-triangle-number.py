class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        
        nums.sort()
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    cnt += j - i
                    j -= 1
                else:
                    i += 1
        
        return cnt
            
"""
https://leetcode.com/problems/valid-triangle-number/discuss/1339248/Python-sort-%2B-2-pointers-solution-explained

对于正整数 a, b, ca,b,c，它们可以作为三角形的三条边，当且仅当：

a+b>c
a+c>b
b+c>a

均成立。如果我们将三条边进行升序排序，使它们满足 a≤b≤c，那么 a + c > b 和 b + c > a 使一定成立的，我们只需要保证 a + b > c

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-triangle-number/solution/you-xiao-san-jiao-xing-de-ge-shu-by-leet-t2td/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
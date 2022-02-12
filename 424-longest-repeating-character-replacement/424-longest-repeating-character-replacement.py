from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 枚举字符串中的每一个位置作为右端点，然后找到其最远的左端点的位置，
        # 满足该区间内除了出现次数最多的那一类字符之外，剩余的字符（即非最长重复字符）数量不超过 k 个。
        # 如果k够用来替换的话，right右移1步，窗口变大（当前维护的最大值变大，不消耗k；当前维护的最大值不变，将消耗k）；
        # 如果k不够用来替换的话，left和right都右移一步，窗口不变（我们已经不关心比当前小的情况了）。
        # 从这个角度来说，也不难理解最后答案是right-left（最后窗口的大小，可扩充的最大窗口）。
        # 作者：LeetCode-Solution
        # 链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/ti-huan-hou-de-zui-chang-zhong-fu-zi-fu-n6aza/

        d = defaultdict(int)
        maxlen = 0
        
        start = 0       
        for end, char in enumerate(s):
            d[char] += 1
            maxf = max(d.values())
            
            if (end - start + 1) - maxf <= k:
                maxlen = max(maxlen, end - start + 1)
                
            else: # (end - start + 1) - maxf > k:
                d[s[start]] -= 1
                start += 1
                
        return maxlen            
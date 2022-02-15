class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        cnt = collections.Counter(s)
        
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and cnt[stack[-1]] >= 1:
                    stack.pop()
                stack.append(c)
            cnt[c] -= 1
        
        return ''.join(stack)

"""
1.题目要求字典排序， 则结果中第一个字母的字典序靠前的优先级最高---贪心
2.因为不能打乱相对位置---即输入中排在输出第一个字母位置前的字母都不能出现，所以要在保证每个字母至少出现一次的前提下再考虑字典序排列
3.根据第1点可以考虑使用单调栈来保证字典序排列,根据第2点我们给元素出栈时加上限制条件,只有在栈顶元素字典序靠后，==且在之后还有出现次数才弹出栈==.同时压栈时应该注意栈中没有出现过该元素才能压栈.
若输入为bcacc
1. b 入栈
2. c 入栈时因为字典序靠后,且栈中没出现过c,直接压栈
3. a 入栈,因为 a 的字典序列靠前且a没有出现过,此时要考虑弹出栈顶元素.
元素 c 因为在之后还有 至少一次 出现次数，所以这里可以弹出.
元素 b 之后不再出现,为了保证至少出现一次这里不能再舍弃了.
4. c 入栈时依然因为字典序靠后且栈中没出现过直接压栈
5. c 入栈时栈中已经出现过c,跳过该元素
输出结果为 bac

作者：programming
链接：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-kan-jiu-hui-jiu-chai-shou-ba-shou-jia-miqw/

字典序：字典序是 按照单词出现在字典中的顺序 比较两个字符串的方法。
首先比较第 1 个字符的 ASCII 码：

如果不同，则第 1 个字符 ASCII 码较小的字符，整体字典序更靠前；
如果相同，则继续比较第 2 个字符，……
如此继续，比较整个字符串的大小。


作者：liweiwei1419
链接：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/zhan-by-liweiwei1419/

"""
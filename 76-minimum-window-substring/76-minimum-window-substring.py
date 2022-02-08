class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        如果hs哈希表中包含ht哈希表中的所有字符，并且对应的个数都不小于ht哈希表中各个字符的个数，那么说明当前的窗口是可行的，可行中的长度最短的滑动窗口就是答案。
        '''
        # goal: substring of s have every char in t (include duplicates)
        
        # if t or s is empty
        if not t or not s:
            return ""
        
        # if target is longer than s string
        if len(s)<len(t):
            return ""
        
        hs, ht = defaultdict(int), defaultdict(int)#初始化新加入key的value为0
        for char in t:
            ht[char] += 1
        res = "" 
        left, right = 0, 0 #滑动窗口
        cnt = 0 #当前窗口中满足ht的字符个数
        while right<len(s):
            hs[s[right]] += 1
            if hs[s[right]] <= ht[s[right]]: #必须加入的元素
                # cnt维护的是s字符串[j,i]区间中满足t字符串的元素的个数，记录相对应字符的总数。
                # 新加入的字符s[i]必需，则cnt++。
                cnt += 1 #遇到了一个新的字符先加进了hs，所以相等的情况cnt也+1
            while left<=right and hs[s[left]] > ht[s[left]]:#窗口内元素都符合，开始压缩窗口
                # 我们向右扩展滑动窗口的同时也不能忘记收缩滑动窗口。
                # 因此当hs[s[j]] > ht[s[j]时，说明hs哈希表中s[j]的数量多于ht哈希表中s[j]的数量，此时我们就需要向右收缩滑动窗口，j++并使hs[s[j]]--，即hs[s[j ++ ]] --。
                hs[s[left]] -= 1
                left += 1
            if cnt == len(t):
                if not res or right-left+1<len(res): 
                    # res为空或者遇到了更短的长度
                    # 当cnt == t.size时，说明此时滑动窗口包含符串 t 的全部字符。我们重复上述过程找到最小窗口即为答案。
                    res = s[left:right+1]
            right += 1
        return res

# 作者：lin-shen-shi-jian-lu-k
# 链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/leetcode-76-zui-xiao-fu-gai-zi-chuan-cja-lmqz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # hashmap
        
        words.sort(key=lambda w: (-len(w), w), reverse = True)
        longest = ""
        seen = set([""])
        
        for word in words:
            if word[:-1] in seen:
                longest = word
                seen.add(word)
        return longest

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-word-in-dictionary/solution/ci-dian-zhong-zui-chang-de-dan-ci-by-lee-k5gj/

        
        # trie! (to do!) 字典树 「208. 实现 Trie (前缀树) 的官方题解」，
        words.sort(key = lambda word : (-len(word), word))
        
        for word in words:
            if all(word[:k] in words for k in range(1, len(word))):
                return word
        
        return ""
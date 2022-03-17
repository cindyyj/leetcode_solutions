class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=lambda x:(-len(x), x), reverse=True)
        
        longest = ""
        seen = set([""])
        for w in words:
            if w[:-1] in seen:
                seen.add(w)
                longest = w
        
        return longest
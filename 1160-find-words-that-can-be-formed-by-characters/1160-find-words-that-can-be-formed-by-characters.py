class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        total_len = 0
        cnt = Counter(chars)
        
        for w in words:
            if Counter(w) <= cnt:
                total_len += len(w)
        
        return total_len
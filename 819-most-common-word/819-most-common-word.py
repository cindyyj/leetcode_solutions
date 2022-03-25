class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # This solution doesn't work in the case of contracted words. 
        # So this solution would fail the test case "Don't tell me you don't want to." It would return "don" instead of "don't".
        text = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        cnt = Counter()
        
        banned = set(banned)        
        for w in text.split():
            if w not in banned:
                cnt[w] += 1
        
        # sort dict are actually sorting its key!
        sorted_cnt = sorted(cnt, key=lambda x: -cnt[x])
        return sorted_cnt[0]
                
        
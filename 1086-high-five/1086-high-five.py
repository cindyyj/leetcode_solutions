class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        
        for i, score in items:
            scores[i].append(score)
        
        ans = []
        for i in sorted(scores):
            ans.append([i, sum( sorted(scores[i], reverse=True)[:5] ) // 5])
        
        return ans
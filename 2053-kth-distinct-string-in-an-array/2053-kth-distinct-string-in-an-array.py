class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        distinct = [w for w in arr if cnt[w] == 1]
        return "" if len(distinct) < k else distinct[k - 1]
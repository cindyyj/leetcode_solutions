class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = int("".join(map(str, num))) + k
        return list(map(int, str(ans)))
        
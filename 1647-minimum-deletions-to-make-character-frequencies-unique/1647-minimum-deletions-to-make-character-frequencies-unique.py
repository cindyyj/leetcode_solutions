class Solution:
    def minDeletions(self, s: str) -> int:
        # Greedy works since we can only delete characters (we cannot add or replace characters).
        # So, count each character first. For each 26 characters, check if it's count is already used. 
        # If so, delete characters until you find unused count, or reach zero.
        # https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927549/C%2B%2BJavaPython-3-Greedy
        cnt, res, used = collections.Counter(s), 0, set()
        for char, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # genius solution
        # https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination
        return s in (2 * s)[1:-1]
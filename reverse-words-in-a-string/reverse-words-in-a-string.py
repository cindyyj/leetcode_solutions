class Solution:
    def reverseWords(self, s: str) -> str:
        # https://leetcode.com/problems/reverse-words-in-a-string/discuss/737124/Python-2-Solutions%3A-Oneliner-%2B-Inplace-for-list-of-chars-explained
        # one-liner
        return ' '.join(s.split()[::-1])
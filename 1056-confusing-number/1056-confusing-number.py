class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation = {"0": 0, "1": 1, "6": 9, "8": 8, "9": 6}
        num = 0

        for i, ch in enumerate(str(n)):
            if ch not in rotation:
                return False
            else:
                num += rotation[ch] * 10 ** i

        return num != n
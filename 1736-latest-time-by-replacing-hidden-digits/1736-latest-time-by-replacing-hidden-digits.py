class Solution:
    def maximumTime(self, time: str) -> str:
        ls = list(time)
        for i, c in enumerate(ls):
            if c == '?':
                if i == 0:
                    ls[i] = '2' if ls[1] <= '3' or ls[1] == '?' else '1'
                elif i == 1:
                    ls[i] = '3' if ls[0] == '2' else '9'
                elif i == 3:
                    ls[i] = '5'
                elif i == 4:
                    ls[i] = '9'
        return ''.join(ls)        
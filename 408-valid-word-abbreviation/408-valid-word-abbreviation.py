class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # 数字不能有前导零 no leading zeros
        # two pointer
        
        i = j = 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',            
        }
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        last = mapping[digits[-1]]
        
        return [ prev_c + last_c for prev_c in prev for last_c in last]
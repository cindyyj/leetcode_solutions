class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        
        # for case when num != 0
        if list(str(num))[-1] == '0':
            return False
        
        return True
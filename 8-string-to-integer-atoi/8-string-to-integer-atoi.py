class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Returns a copy of the string with both leading and trailing characters removed.
        ls = list(s.strip())
        if len(ls) == 0 : return 0
       
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        
        res, i = 0, 0
        while i < len(ls) and (ls[i].isdigit()) :
            res = res*10 + int(ls[i])  # ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * res,2**31-1))
        
        
#         # 确定有限状态机（deterministic finite automaton, DFA
        
#         INT_MAX = 2**31 - 1    
#         INT_MIN = -2**31
#         s = s.lstrip()      #清除左边多余的空格
#         num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
#         num = num_re.findall(s)   #查找匹配的内容
#         num = int(*num) #由于返回的是个列表，解包并且转换成整数
#         return max(min(num,INT_MAX),INT_MIN)    #返回值       
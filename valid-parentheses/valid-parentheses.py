class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        brackets_dict = {
            "(": ")", 
            "{": "}",
            "[": "]",
        }
        
        for char in s:
            if char in brackets_dict.keys():
                stack.append(char)
            else:
                if stack ==[]:
                    return False
                top = stack.pop()
                if char != brackets_dict[top]:
                    return False
        return stack==[]
            
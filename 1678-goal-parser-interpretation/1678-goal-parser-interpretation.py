class Solution:
    def interpret(self, command: str) -> str:
        
        replace_map = {
            '()':'o',
            '(al)':'al'
        }
        
        def replace_with_map(command: str, pattern: str) -> str:
            return command.replace(pattern, replace_map[pattern])
        
        return reduce(replace_with_map, replace_map, command)
        
        
        # return command.replace("()", "o").replace("(al)", "al")
        
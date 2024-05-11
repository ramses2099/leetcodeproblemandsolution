class Solution:
    """1678. Goal Parser Interpretation"""
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")
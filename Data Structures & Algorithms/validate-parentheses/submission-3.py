class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}
        for i in s:
            if i in pairs:
                top = stack.pop() if stack else None
                if pairs[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack

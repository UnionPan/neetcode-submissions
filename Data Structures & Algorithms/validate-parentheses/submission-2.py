class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'}': '{', ']': '[', ')': '('}
        for c in s:
            if c in parentheses.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != parentheses[c]:
                    return False
                else:
                    stack.pop()
        return not stack
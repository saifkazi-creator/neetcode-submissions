class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or match[ch] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
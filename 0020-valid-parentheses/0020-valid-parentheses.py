class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and (char == ')' or char == ']' or char == '}'):
                last = stack[-1]
                if (char == ')' and last != '(') or (char == ']' and last != '[') or (char == '}' and last != '{'):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True
        
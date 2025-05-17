def is_valid(s: str) -> bool:
    stack = []
    closeToOpen = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in closeToOpen:  # in checks the keys not the values
            if stack and stack[-1] == closeToOpen[c]:  # stack[-1] is the top of the stack
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

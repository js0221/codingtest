# solution 1
def solution(s):
    stack = []
    
    for c in s:
        if stack:
            if (stack[-1] == '{' and c == '}') or \
            (stack[-1] == '(' and c == ')') or \
            (stack[-1] == '[' and c == ']'):
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    return bool(stack == [])
    
    
# solution 2
def solution(s):
    stack = []

    for c in s:
        if stack and 0 < ord(c) - ord(stack[-1]) <= 2:
            stack.pop()
        else:
            stack.append(c)

    return True if len(stack) == 0 else False

def solution(s):
    stack = []
    
    for c in s:
        while stack and stack[-1] < c:
            stack.pop()
        stack.append(c)
    
    return ''.join(stack)

from collections import deque
def solution(m, n, infests, vaccinateds):
    ways = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    board = [[0] * n for _ in range(m)]
    
    # 감염 1, 백신 -1, 없음 0
    for i, j in vaccinateds:
        board[i - 1][j - 1] = -1
    for i, j in infests:
        board[i - 1][j - 1] = 1
    
    # 탐색 전 : 어느 직원이든지 감염이나, 백신 상태일때
    for i in board:
        if 0 in i:
            break
    else:
        return 0
    
    # 탐색
    queue = [(x - 1, y - 1) for x, y in infests]
    queue = deque(queue)
    while queue:
        x, y = queue.popleft()
        
        for wx, wy in ways:
            new_x, new_y = x + wx, y + wy 
            if 0 <= new_x < m and 0 <= new_y < n and board[x][y] >= 1 and board[new_x][new_y] == 0:

                board[new_x][new_y] = board[x][y] + 1
                queue.append((new_x, new_y))
        
    # 탐색 후 : 빈칸이 있을 때
    for i in board:
        if 0 in i:
            return -1
    
    return max(map(max, board)) - 1

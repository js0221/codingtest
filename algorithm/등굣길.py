# solution 1
def solution(m, n, puddles):
    area = [[0] * (m + 1) for _ in range(n+1)] # 지도
    area[1][1] = 1 # 시작점
    
    # 웅덩이
    for x, y in puddles:
        area[y][x] = -1
        
    # 이중 루프
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if area[y][x] == -1: # 웅덩이이면
                area[y][x] = 0 # 합산할 때 계산이 안되게 0으로 바꿔준다
                continue # 그리고 건너뜀
            
            # 현재 좌표로 오는 경우의 수는 왼쪽과 위에 있는 값을 더해준다.
            area[y][x] += (area[y][x - 1] + area[y - 1][x]) % 1000000007
            
    return area[n][m]


# solution 2
'''
board[i][j] += 가 아니다. 그래서 (1, 1)인 경우를 따로 처리해야됨
처리를 안하면, (0, 1) + (1, 0) =  0 + 0 = 0이 된다.
if문 검사를 하기 떄문에 solution1 보다 효울성이 떨어지긴 함
'''
def solution(m, n, puddles):
    board = [[0] * (n + 1) for _ in range(m + 1)]
    for x, y in puddles:
        board[x][y] = float('inf')
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # solution1과 다른 부분
            if i == 1 and j == 1:
                board[1][1] = 1
                continue
            
            if board[i][j] == float('inf'):
                board[i][j] = 0
                continue
                
            # solution1과 다른 부분
            board[i][j] = board[i - 1][j] + board[i][j - 1] 
    
    return board[m][n] % 1000000007

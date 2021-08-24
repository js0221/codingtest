# solution 1
from collections import deque
def solution(n, m, image):
    # 1. 방문한 노드, 방향 리스트 설정
    answer = 0
    visited = [[0] * m for _ in range(n)] # [[0]*m]*n 에러
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # []안에, 튜플 사용
    
    # 2. 탐색 (for)
    for i in range(n):
        for j in range(m):
            
            #---------------------------------
            # 방문한 곳을 찾아, 이것은 넘어가고, if문 나와서 방문하지 않은 노드에 대해 처리한다.
            # 들여쓰기를 줄일 수 있다
            if image[i][j] == float('inf'):
                continue
            target_color = image[i][j]
            queue = deque([(i, j)])
            '''
            # 방문하지 않은 노드만 탐색
            if visited[i][j] == 0: 
                # 방문표시 & 정답 += 1
                visited[i][j] = 1
                answer += 1
                
                queue = deque([[i,j]])
                
                # 3. 인접노드 탐색
                while queue:
                    ....
            '''
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                  
                    # 이동 좌표 : 자주 사용하므로 변수 할당
                    px = x + dx
                    py = y + dy
                    
                    if px >= n or px < 0 or py >= m or py < 0:
                        continue
                    if image[px][py] == target_color:
                        image[px][py] = float('inf')
                        queue.append((px, py))
            answer += 1

    return answer


# solution 2
from collections import deque
def solution(n, m, image):
    answer = 0
    way = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    board = [[0] * m for _ in range(n)]
    queue = deque()    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                queue.append((i, j))
                board[i][j] = 1
                answer += 1
            
            while queue:
                x, y = queue.pop()
                for wx, wy in way:
                    new_x, new_y = x + wx, y + wy
                    
                    if 0 <= new_x < n and 0 <= new_y < m and image[new_x][new_y] == image[x][y] and board[new_x][new_y] == 0:
                    # target_color로 따로 변수를 설정 안할 경우 image를 건드리면 안됨
                    # board[new_x][new_y]를 안하면, 큐에서 new_x, new_y를 검사할 떄, x,y를 또 큐에 넣고 다시 계속 반복됨
                        queue.append((new_x, new_y))
                        board[new_x][new_y] = 1
                    
    return answer

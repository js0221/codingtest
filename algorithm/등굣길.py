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

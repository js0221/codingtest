# solution 1
from collections import deque
def solution(dirs):
    answer = 0
    way = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    l_move = list()
    current = (5, 5)
    
    for d in dirs:
        new = (current[0] + way[d][0], current[1] + way[d][1])
        
        if 0 <= new[0] < 11 and 0 <= new[1] < 11:
            move = (sorted((current[0], new[0])), sorted((current[1], new[1])))
            
            if move not in l_move:
                l_move.append(move)
                answer += 1
        
            current = new
    return answer
  

# solution 2

  
def solution(dirs):
    position = (0, 0) # 시작 좌표를 0, 0으로 지정
    
    command_dict = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    
    check = set() # 좌표를 키로 사용하는 해시 생성
    for command in dirs: # O(dirs)
        direction = command_dict[command]
        next_position = tuple(map(sum, zip(position, direction)))
        
        y, x = next_position
        if -5 <= y <= 5 and -5 <= x <= 5:
            check.add(tuple(sorted([position, next_position])))
            '''
            * 대각선 이동이 없기때문에,  x는 오름차순, y는 내림차순 정렬되는 경우는 없다
            * x 정렬하고, 같으면 y 정렬 (sort는 원소 순서대로 비교하면서 정렬)
            '''
            position = next_position

    return len(check)
  
  
  
# solution 3
# 작은 값을 앞으로 정렬하기 위해서 x-1, x, x+1 | y-1, y, y+1 순서로 두게함
# 0 -> 1이나, 1 -> 0이나 같은 경로임
def solution(dirs):
    x, y = 0, 0 # 시작 좌표를 0, 0으로 지정
    check = dict() # 좌표를 키로 사용하는 해시 생성
    for command in dirs: # O(dirs)
        if command == 'U' and y < 5: # 위로
            check[(x, y, x, y+1)] = True # 현재 좌표, 이동할 좌표
            y += 1
        elif command == 'D' and y > -5: # 아래로
            check[(x, y-1, x, y)] = True # 이동할 좌표, 현재 좌표
            y -= 1
        elif command == 'R' and x < 5: # 오른쪽으로
            check[(x, y, x+1, y)] = True # 현재 좌표, 이동할 좌표
            x += 1
        elif command == 'L' and x > -5: # 왼쪽으로
            check[(x-1, y, x, y)] = True # 이동할 좌표, 현재 좌표.
            x -= 1

    return len(check) # 추가된 값들이 곧 방문 길이
  '''
  check 출력
  {(0, 0, 0, 1): True, (-1, 1, 0, 1): True, (-1, 1, -1, 2): True, (-1, 2, 0, 2): True, (0, 2, 1, 2): True, (1, 1, 1, 2): True, (0, 1, 1, 1): True}
  
  - 새로운 경로이면 딕셔너리 추가
  - 딕셔너리 추가 : dict[key] = value
  '''

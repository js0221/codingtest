def solution(board, nums):    
    answer = 0
    N = len(board)
    nums = set(nums)
        
    for y in range(N):
        for x in range(N):
            if board[x][y] in nums:
                board[x][y] = 0
                
    answer += len([i for i in board if sum(i) == 0])
    answer += len([i for i in zip(*board) if sum(i) == 0])
    answer += int(sum(board[i][i] for i in range(N)) == 0)
    answer += int(sum(board[N - 1 - i][i] for i in range(N)) == 0)
    
    return answer

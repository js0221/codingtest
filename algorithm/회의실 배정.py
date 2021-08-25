def solution(arr):
    arr.sort(key = lambda x : (x[1], x[0]))
    answer, end = 0, 0
    
    for s, e in arr:
        if s >= end:
            answer += 1
            end = e
    return answer


# 백준 solution
n = int(input())
time = [tuple(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x : (x[1], x[0]))
answer = 0

prev_finish = 0
for start, finish in time:
    if prev_finish > start:
        continue
    prev_finish = finish
    answer += 1

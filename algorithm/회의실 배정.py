def solution(arr):
    arr.sort(key = lambda x : (x[1], x[0]))
    answer, end = 0, 0
    
    for s, e in arr:
        if s >= end:
            answer += 1
            end = e
    return answer

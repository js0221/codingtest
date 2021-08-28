def solution(lottos, win_nums):
    answer, zero, same = 0, 0, 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for l in lottos:
        if l == 0:
            zero += 1
        if l in win_nums:
            same += 1
    
    return rank[zero + same], rank[same]

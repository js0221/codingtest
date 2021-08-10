# solution 1
from itertools import combinations
def erathos(c):
    era = [False, False] + [True] * (c - 1)
    for i in range(2, int(c ** 0.5) + 1):
        era[i * 2::i] = [False] * ((c - i) // i)
        
    return int(era[c] == True)


def solution(nums):
    answer = 0
    comb = list(map(sum, combinations(nums, 3)))

    for c in comb:
        answer += erathos(c)
    return answer


# solution 2
def erathos(n):
    era = [False, False] + [True] * (n -1)
    for i in range(2, int(n ** 0.5) + 1):
        era[i * 2::i] = [False] * ((n-i) // i)
    return era[n]
    
    
def solution(nums):
    answer = 0
    pick = list(combinations(nums, 3))
    for i in pick:
        s = sum(i)
        
        if erathos(s):
            answer += 1
            
    return answer

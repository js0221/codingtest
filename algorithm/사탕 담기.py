from itertools import combinations
def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        answer += list(map(sum, combinations(weights, i))).count(m)
    return answer

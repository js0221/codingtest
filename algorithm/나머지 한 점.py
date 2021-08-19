# Counter는 dictionary에서 가져옴
from collections import Counter 

def solution(v):
    answer = []

    x = [x for x, _ in v]
    y = [y for _, y in v]

    answer += [key for key, value in Counter(x).items() if value == 1]
    answer += [key for key, value in Counter(y).items() if value == 1]

    return answer

# solution 2
from collections import Counter
def solution(v):
    answer = []
    for i in zip(*v):
        answer += [idx for idx, val in Counter(i).items() if val == 1]
    return answer

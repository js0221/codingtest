from collections import defaultdict
def solution(participant, completion):
    d = defaultdict(int)

    for i in participant:
        d[i] += 1
        
    for i in completion:
        d[i] -= 1
        
    for key, value in d.items():
        if value > 0:
            return key

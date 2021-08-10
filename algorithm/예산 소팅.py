# solution 1
def solution(d, budget):
    answer, d_sum = 0, 0
    d.sort()    
    
    for i in d:
        d_sum += i
        if d_sum <= budget:
            answer += 1
        else:
            break
    
    return answer
  
# solution 2
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

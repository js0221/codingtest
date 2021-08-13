def solution(scores):
    answer = ''
    
    num = 0
    for i in zip(*scores):
        i = list(i)
        student = len(i)
        if (i[num] == max(i) and i.count(max(i)) == 1) or (i[num] == min(i) and i.count(min(i)) == 1):
            i[num] = 0
            student -= 1
        num += 1
            
        avg = sum(i) / student
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
            
    return answer

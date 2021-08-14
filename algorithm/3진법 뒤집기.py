# solution 1
def solution(n):
    three = ''
    while n > 0:
        n, m = divmod(n, 3)
        three += str(m)
    return int(three, 3)

  
# solution 2
def solution(n):
    answer = 0
    
    three = ''
    while n > 0:
        n, m = divmod(n, 3)
        three = str(m) + three
    
    for i in range(len(three)):
        answer += (3 ** i) * int(three[i])

    return answer

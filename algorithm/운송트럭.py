# dict(list()) : 리스트 바로 딕셔너리 만들기
# 무게 합이 맥스를 채우면 트럭 한대 추가 (if tmp < 0)
def solution(max_weight, specs, names):
    spec = dict(specs)
    
    answer = 1
    tmp = max_weight
    
    for n in names:
        tmp -= int(spec[n])
        if tmp < 0:
            answer += 1
            tmp = max_weight - int(spec[n])

    return answer

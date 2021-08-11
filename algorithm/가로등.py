from math import ceil
def solution(l, v):
    light = set()
    v.sort()
    
    # 기둥 처리
    for i in range(1, len(v)):
        light.add(ceil((v[i] - v[i - 1]) / 2))
    
    # 양쪽 끝 처리
    light.add(v[0])
    light.add(l - v[-1])
    
    return max(light)

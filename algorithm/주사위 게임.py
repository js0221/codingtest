# solution 1
def solution(monster, S1, S2, S3):
    case = []
    for s1 in range(1, S1 + 1):
        for s2 in range(1, S2 + 1):
            for s3 in range(1, S3 + 1):
                case.append(s1 + s2 + s3 + 1)
    
    m = 0
    for i in monster:
        m += case.count(i)
        
    return int((1 - (m / (s1 * s2 * s3))) * 1000)  
  

# solution 2
from itertools import product
def solution(monster, S1, S2, S3):
    l1 = list(range(1, S1 + 1))
    l2 = list(range(1, S2 + 1))
    l3 = list(range(1, S3 + 1))
    
    a = list(product(l1, l2, l3))
    print(a)
    
    # lc : list_combination - 세 개의 리스트 조합의 경우, 그것에 대한 합 // len(lc)
    # 도착하는 지점은 1에서 sum(c)칸을 건너는 것이므로 sum(c) + 1
    lc = [sum(c) + 1 for c in product(l1, l2, l3)]
    
    # mc : monster_case - lc에 몬스터에 도착하는 경우가 있는 경우 // sum(mc)
    mc = [lc.count(m) for m in monster]

    return int((len(lc) - sum(mc)) / len(lc) * 1000)

# solution 3
from itertools import product

def solution(monster, S1, S2, S3):
    p = product(range(S1), range(S2), range(S3))
    case = len([x for x in p if sum(x) + 4 not in monster])
    return int(case / (S1 * S2 * S3) * 1000)

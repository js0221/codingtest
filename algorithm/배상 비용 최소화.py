# sol1
from heapq import _heapify_max, _heappop_max
    def solution(no, works):
    if no >= sum(works): # 일의 총 시간 합이, no보다 작으면 0으로 만들 수 있다.
        return 0
        
     _heapify_max(works) # 제일 큰 수 찾기
    for _ in range(no):
        max_works = _heappop_max(works)
        max_works -= 1
        works.append(max_works)

    return sum([i ** 2 for i in works])


# sol2
from heapq import heapify, heapreplace
def solution(no, works):
    if no > sum(works):
        return 0
    
    work = [-i for i in works]
    heapify(work)
    
    for _ in range(no):
        # heapreplace : 팝 후 푸시
        # heappushpop : 푸시 후 팝
        # 마이너스로 값을 넣었기때문에 가장 작은 값에 +1을 해주면 절댓값이 줄어듬
        heapreplace(work, work[0] + 1)
        
    return sum([i ** 2 for i in work])

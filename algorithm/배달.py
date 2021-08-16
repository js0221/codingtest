from heapq import heappop, heappush

def solution(N, road, K):
    table = [float('inf')] * (N + 1)
    table[1] = 0
    queue = [(1, 0)]
    
    while queue:
        current, current_cost = heappop(queue)
        
        for start, end, cost in road:
            next_cost = current_cost + cost
            if start == current and next_cost < table[end]:
                table[end] = next_cost
                heappush(queue, (end, next_cost))
            elif end == current and next_cost < table[start]:
                table[start] = next_cost
                heappush(queue, (start, next_cost))
    
    return len([i for i in table if i <= K])

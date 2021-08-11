def solution(numbers):
    numbers.sort(key = lambda x: str(str(x) * 4)[:4], reverse=True)
    return '0' if numbers[0] == 0 else ''.join(map(str, numbers))
  
'''
앞의 숫자가 같을 경우
1. 가장 큰수는 1000이다
2. 배치되는 수 중에서 배치되는 수보다 큰 수는 길어봐야 반복되는 수이다.
-> 4개를 계속 반복하게 하여, 4개까지 슬라이스
'''

# solution1
def erathos(n):
    era = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        era[i * 2::i] = [False] * ((n - i) // i)
        # 1. i : 2부터 판별하고자 하는 수의 제곱근까지 확인
        # 2. [i * 2::i] : i의 두번째 배수 부터 가져옴, 2i, 3i, 4i...
        # 3. (n-i)//i : 배수 부분의 숫자들만 가져온 것 개수
        # (2i ~ n 중에서 i의 배수니까 i로 나눠주면 개수가 나옴)
        # 4. 슬라이싱 한 부분만 False로 바뀜
        
# solution2
def get_primes(n):
    is_prime = [False, False] + [True] * (n - 2)

    for i in range(int(n // 2) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
                
    return [i for i, p in enumerate(is_prime) if p]

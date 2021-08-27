def make_trie(words):
    root = {} # 먼저 루트 노드를 설정할 변수를 만들고
    for word in words: # Trie를 구성하기 위한 루프를 돌립니다.
        current = root # 루트부터 시작합니다.
        for letter in word: # 단어의 글자를 하나씩 추출한 후
            current.setdefault(letter, [0, {}]) # 값을 넣습니다. 리스트의 첫 번째 값은 학습된 단어가 몇 개인지 카운팅하고 두 번째 값은 트리 구조로 이용할 노드 값 입니다.
            current[letter][0] += 1 # 카운팅을 위해 1 더해줍니다.
            current = current[letter][1] # current는 letter에 해당되는 노드로 이동합니다.
            
    return root

def solution(words):
    answer = 0
    trie = make_trie(words) # Trie를 만들어 줍니다.
    
    for word in words: # 입력받은 수 만큼 루프를 돕니다.
        current = trie # 루트부터 시작합니다.
        for index, letter in enumerate(word):
            if current[letter][0] <= 1: # 단어가 하나 이하로 남을 경우
                break
            current = current[letter][1] # 다음 노드로 이동합니다.
        answer += index + 1
        
    return answer

# solution 1
def solution(n, words):
    word = words[0]
    check = {words[0]}

    for i in range(1, len(words)):
        if word[-1] == words[i][0] and words[i] not in check:
            word = words[i]
            check.add(words[i])
        else:
            return (i % n) + 1, (i // n) + 1
    else:
        return 0, 0
    
    
# solution 2
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

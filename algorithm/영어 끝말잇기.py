def solution(n, words):
    check = set()
    word = words[0]
    check.add(words[0])
    saram = 0
    
    for i in range(1, len(words)):
        saram += 1
        if word[-1] == words[i][0] and words[i] not in check:
            word = words[i]
            check.add(words[i])
        else:
            break
    else:
        return 0, 0

    order, num = divmod(saram, n)
    return num + 1, order + 1


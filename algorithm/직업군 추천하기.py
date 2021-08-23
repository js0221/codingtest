def solution(table, languages, preference):
    score = {l.split()[0] : 0 for l in table}
    chart = [i.split() for i in table]

    for i in chart:
        for l, p in zip(languages, preference):
            try:
                score[i[0]] += ((6 - i.index(l)) * p)
            except:
                continue

    score = sorted([(key, value) for key, value in score.items()], key=lambda x: (-x[1], x[0]))
    return score[0][0]

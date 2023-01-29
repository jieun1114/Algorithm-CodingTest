from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = 0
    # n개의 자릿수 정하기

    for combi in combinations_with_replacement(range(11), n):

        info2 = [0] * 11

        for i in combi:
            info2[10 - i] += 1  # 낮은 점수부터 세팅

        apeach, lion = 0, 0

        for i in range(11):
            if info[i] == info2[i] == 0:
                continue
            elif info[i] >= info2[i]:
                apeach += 10 - i
            else:
                lion += 10 - i

        if lion > apeach:
            diff = lion - apeach
            if diff > max_diff:
                max_diff = diff
                answer = info2

    return answer
def solution(friends, gifts):
    answer = 0

    name = list()
    present = [[0] * len(friends) for _ in range(len(friends))]
    nextmonth = [0] * len(friends)
    give = [0] * len(friends)
    take = [0] * len(friends)

    # friend 를 인덱스로 매칭
    for friend in friends:
        name.append(friend) # 0: muzi, 1: ryan, 2: frodo, 3:neo

    # 선물지수 구하기
    for gift in gifts:
        give[name.index(gift.split()[0])] += 1
        take[name.index(gift.split()[1])] += 1

    # 선물지수 프린트
    for i in range(len(friends)):
       print(name[i], give[i]-take[i])

    # 선물기록 배열로 만들기
    for giver in range(len(friends)):
        for receiver in range(len(friends)):
            if giver != receiver:
                present[giver][receiver] = gifts.count(name[giver] + " " + name[receiver])

    # friend별 다음달에 받을 선물 수 구하기
    for giver in range(len(friends)):
        nextmonth[giver] = 0
        for receiver in range(len(friends)):
            if giver != receiver:
                if present[giver][receiver] == present[receiver][giver]:
                    # 선물지수로 판단
                    if give[giver] - take[giver] > give[receiver] - take[receiver]:
                        nextmonth[giver] += 1
                elif present[giver][receiver] > present[receiver][giver]:
                    nextmonth[giver] += 1

        answer = max(answer, nextmonth[giver])

    print(nextmonth)
    print(answer)
    return answer

solution(["joy", "brad", "alessandro", "conan", "david"],["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
import itertools

def solution(users, emot):
    answer = []
    sales = [10, 20, 30, 40]

    cases = itertools.product(sales, repeat=len(emot))
    cases = list(cases)
    #print(cases)
    pp = []

    for case in cases:
        t_plus = 0
        t_profit = 0
        for user in users:  # [40, 10000]
            per, limit = user[0], user[1]
            price = 0
            for i, c in enumerate(case):  # (10, 10)
                if c < per:
                    continue
                price += int(emot[i]*(1 - c * 0.01))
                if price >= limit:
                    t_plus += 1
                    price = 0
                    break
            t_profit += price
        pp.append([t_plus, t_profit])

    b = sorted(pp, key=lambda x:(-x[0],-x[1]))
    print(b)
    answer = b[0]
    print(answer)

    return answer

solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900])
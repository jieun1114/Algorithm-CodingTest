import datetime as dt
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []

    date_today = dt.datetime.strptime(today, '%Y.%m.%d')

    term_month = [0] * 26
    for term in terms:
        term_month[ord(term.split()[0]) - 65] = int(term.split()[1])

    print(term_month)

    for i, pvc in enumerate(privacies):
        pvc_day = pvc.split()[0]  # 2021.05.02
        pvc_term = pvc.split()[1]  # A

        date_pvc = dt.datetime.strptime(pvc_day, '%Y.%m.%d')
        print(date_pvc)
        store_m = term_month[ord(pvc_term) - 65]

        date_expire = date_pvc + relativedelta(months=store_m)

        if date_expire <= date_today:
            answer.append(i+1)

    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
      
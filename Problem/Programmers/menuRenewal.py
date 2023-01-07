from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []

    dic = defaultdict(int)
    menus = []
    courses = [[] for _ in range(11)]

    for order in orders:
        for num in course:  # [2,3,4]
            clist = list(order)  # ABCFG
            c = combinations(clist, num)
            combi_list = list(c)  # list(c) [('A','B'),('A','C'),..]
            for menu in combi_list:
                str = ""
                str = str.join(menu)  # AB
                str = "".join(sorted(str))
                if str not in menus:
                    menus.append(str)
                dic[str] += 1

    # 두명이상 주문한 메뉴만
    for menu in menus:
        if dic[menu] >= 2:
            courses[len(menu)].append([menu, dic[menu]])

    for o in course:
        if len(courses[o]) > 0:
            s_course = sorted(courses[o], key=lambda x: -x[1])
            max_order = s_course[0][1]
            for cs in s_course:
                if cs[1] == max_order:
                    answer.append(cs[0])
                else:
                    break

    answer.sort()
    print(answer)
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])